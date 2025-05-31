# -*- coding: utf-8 -*-

import joblib
import pandas as pd
import numpy as np
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
MODELS_DIR = os.path.join(BASE_DIR, "models")

class PredictionService:
    """
    Lớp này quản lý việc tải mô hình, scaler và các thành phần tiền xử lý,
    cũng như cung cấp hàm để dự đoán giá điện thoại mới.
    """
    def __init__(self):
        self.best_lgbm_model = None
        self.scaler = None
        self.trained_feature_columns = None
        self._load_artifacts()

    def _load_artifacts(self):
        """
        Tải mô hình, scaler và danh sách các cột đặc trưng từ thư mục MODELS_DIR.
        """
        try:
            model_path = os.path.join(MODELS_DIR, 'best_lgbm_regressor.joblib')
            scaler_path = os.path.join(MODELS_DIR, 'scaler.joblib')
            features_path = os.path.join(MODELS_DIR, 'feature_columns.joblib')

            self.best_lgbm_model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            self.trained_feature_columns = joblib.load(features_path)
            print("Mô hình, scaler và cột đặc trưng đã được tải thành công.")
        except FileNotFoundError as e:
            print(f"Lỗi: Không tìm thấy file cần thiết trong thư mục '{MODELS_DIR}'. {e}")
            print("Vui lòng đảm bảo các file 'best_lgbm_regressor.joblib', 'scaler.joblib', 'feature_columns.joblib' có trong thư mục 'models'.")
        except Exception as e:
            print(f"Lỗi khi tải các tài nguyên mô hình: {e}")

    # --- Các hàm tiền xử lý dữ liệu ---
    def _clean_ram(self, item):
        """Làm sạch và chuyển đổi cột RAM."""
        item = str(item).replace('GB', '')
        if '/' in item:
            item = item.split('/')[1]  # Lấy giá trị cao hơn
        return float(item)

    def _clean_front_camera(self, item):
        """Làm sạch và chuyển đổi cột Front Camera."""
        item = [float(i) for i in re.findall(r'\d+', str(item))]
        return max(item) if item else 0.

    def _clean_back_camera(self, item):
        """Làm sạch và chuyển đổi cột Back Camera thành 4 cột riêng biệt."""
        items = str(item).split('+')
        list_camera = [0., 0., 0., 0.]
        for idx, sub_item in enumerate(items):
            if idx == 2:
                if 'macro' not in sub_item.lower():
                    list_camera[2] = float(sub_item.split('MP')[0])
                elif 'macro' in sub_item.lower():
                    list_camera[3] = float(sub_item.split('MP')[0])
            else:
                list_camera[idx] = float(sub_item.split('MP')[0])
        return list_camera

    def _extract_storage(self, item):
        """Trích xuất kích thước lưu trữ từ Model Name."""
        item = str(item).split(' ')[-1]
        if 'GB' in item:
            return int(item.replace('GB', ''))
        elif 'TB' in item:
            return int(item.replace('TB', '')) * 1024
        else:
            return pd.NA  # Trả về NA nếu không tìm thấy GB/TB

    def _extract_processor_brand(self, processor):
        """Nhóm các bộ xử lý theo thương hiệu."""
        processor = str(processor)  # Đảm bảo là string
        if 'Snapdragon' in processor:
            return 'Qualcomm Snapdragon'
        elif 'MediaTek' in processor or 'Dimensity' in processor or 'Helio' in processor:
            return 'MediaTek'
        elif 'Bionic' in processor or 'A' in processor:
            return 'Apple Bionic'
        elif 'Exynos' in processor:
            return 'Samsung Exynos'
        elif 'Tensor' in processor:
            return 'Google Tensor'
        elif 'Unisoc' in processor:
            return 'Unisoc'
        elif 'Kirin' in processor:
            return 'Kirin'
        else:
            return 'Other'

    def preprocess_data(self, raw_data: dict) -> pd.DataFrame:
        """
        Thực hiện tất cả các bước tiền xử lý trên dữ liệu thô đầu vào.
        Đảm bảo các bước này khớp chính xác với quá trình huấn luyện mô hình.
        """
        # Tạo DataFrame từ dữ liệu thô
        df_new = pd.DataFrame([raw_data])

        # 1. Chuyển đổi 'Launched Year'
        df_new['Launched Year'] = pd.to_datetime(df_new['Launched Year'], format='%Y').dt.year.astype('int')

        # 2. Xử lý 'Mobile Weight (g)'
        df_new['Mobile Weight (g)'] = df_new['Mobile Weight'].str.replace('g', '').astype(float)

        # 3. Xử lý 'RAM (GB)'
        df_new['RAM (GB)'] = df_new['RAM'].apply(self._clean_ram)

        # 4. Xử lý 'Front Camera (MP)'
        df_new['Front Camera (MP)'] = df_new['Front Camera'].apply(self._clean_front_camera)

        # 5. Xử lý 'Back Camera' thành 4 cột
        temp_cols = ['Main Camera (MP)', 'Ultra Camera (MP)', 'Telephoto Camera (MP)', 'Macro Camera (MP)']
        df_new[temp_cols] = df_new['Back Camera'].apply(lambda x: pd.Series(self._clean_back_camera(x)))

        # 6. Xử lý 'Battery Capacity (mAh)'
        df_new['Battery Capacity (mAh)'] = df_new['Battery Capacity'].str.replace('mAh', '').str.replace(',', '').astype(int)

        # 7. Xử lý 'Screen Size (inches)'
        df_new['Screen Size (inches)'] = df_new['Screen Size'].apply(lambda x: x.split('inches')[0]).astype(float)

        # 8. Trích xuất 'Storage (GB)' từ 'Model Name'
        df_new['Storage (GB)'] = df_new['Model Name'].apply(self._extract_storage)

        # 9. Xử lý Processor_Brand
        df_new['Processor_Brand'] = df_new['Processor'].apply(self._extract_processor_brand)

        # 10. One-Hot Encoding cho Processor_Brand, Company Name, Country
        categorical_cols_for_ohe = ['Processor_Brand', 'Company Name', 'Country']

        # Tạo OHE cho các cột phân loại từ dữ liệu mới
        df_ohe_new = pd.get_dummies(df_new[categorical_cols_for_ohe].copy(), drop_first=False)

        # Tạo DataFrame cuối cùng với tất cả các cột đặc trưng đã huấn luyện
        final_input_df = pd.DataFrame(0, index=[0], columns=self.trained_feature_columns)

        # Danh sách các cột số đã định nghĩa trong quá trình huấn luyện
        numerical_features_final = [
            'Launched Year', 'Mobile Weight (g)', 'RAM (GB)', 'Front Camera (MP)',
            'Main Camera (MP)', 'Ultra Camera (MP)', 'Telephoto Camera (MP)',
            'Macro Camera (MP)', 'Battery Capacity (mAh)', 'Screen Size (inches)',
            'Storage (GB)'
        ]

        # Điền các giá trị số đã xử lý vào DataFrame cuối cùng
        for col in numerical_features_final:
            if col in final_input_df.columns and col in df_new.columns:
                final_input_df[col] = df_new[col]

        # Điền các giá trị OHE đã xử lý vào DataFrame cuối cùng
        for col in df_ohe_new.columns:
            if col in final_input_df.columns:
                final_input_df[col] = df_ohe_new[col]

        return final_input_df

    def predict_new_phone_price(self, new_phone_data_raw: dict) -> float:
        """
        Dự đoán giá điện thoại mới dựa trên dữ liệu đầu vào thô.

        Args:
            new_phone_data_raw (dict): Dữ liệu điện thoại mới.

        Returns:
            float: Giá điện thoại dự đoán.
        """
        if self.best_lgbm_model is None or self.scaler is None or self.trained_feature_columns is None:
            raise Exception("Mô hình, scaler hoặc cột đặc trưng chưa được tải. Vui lòng kiểm tra log.")

        try:
            processed_data_df = self.preprocess_data(new_phone_data_raw)

            X_processed_array = processed_data_df[self.trained_feature_columns].values

            scaled_data = self.scaler.transform(X_processed_array)

            log_predicted_price = self.best_lgbm_model.predict(scaled_data)[0]

            predicted_price = np.exp(log_predicted_price)
            return predicted_price
        except Exception as e:
            print(f"Lỗi trong quá trình dự đoán: {e}")
            raise

