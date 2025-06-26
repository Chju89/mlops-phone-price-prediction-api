# Dự án Dự đoán Giá Điện thoại (MLOps Pipeline)

---

## 🚀 Tổng quan dự án

Dự án này trình bày một pipeline MLOps hoàn chỉnh cho việc dự đoán giá điện thoại dựa trên các thông số kỹ thuật. Nó bao gồm từ giai đoạn phát triển mô hình (trong notebook Colab) đến triển khai mô hình dưới dạng một API sử dụng FastAPI, được container hóa bằng Docker, và sẵn sàng cho các bước MLOps nâng cao như giám sát và CI/CD.

Mô hình dự đoán được sử dụng là **LightGBM Regressor**, đã được huấn luyện trên một tập dữ liệu về các thông số kỹ thuật và giá điện thoại.

---

## 📂 Cấu trúc thư mục

Dự án được tổ chức gọn gàng để dễ dàng quản lý và mở rộng:

.

├── app/
│   ├── app.py                     # Ứng dụng FastAPI để phục vụ mô hình
│   └── prediction_service.py      # Chứa logic tải mô hình, tiền xử lý và dự đoán
├── models/
│   ├── best_lgbm_regressor.joblib # Mô hình LightGBM đã huấn luyện
│   ├── scaler.joblib              # Scaler dùng để chuẩn hóa dữ liệu
│   └── feature_columns.joblib     # Danh sách các cột đặc trưng đã được huấn luyện
├── notebook/
│   └── mobiles_price_prediction.ipynb # Notebook Google Colab để phát triển và huấn luyện mô hình
├── .dockerignore                  # Các tệp và thư mục sẽ bị bỏ qua khi xây dựng Docker image
├── Dockerfile                     # Hướng dẫn xây dựng Docker image
├── requirements.txt               # Danh sách các thư viện Python cần thiết
└── README.md                      # File hướng dẫn dự án này

---

## 🛠️ Thiết lập môi trường cục bộ

Để chạy dự án này trên máy cục bộ của bạn, hãy làm theo các bước sau:

### 1. Tạo và kích hoạt môi trường Conda

Mở Terminal hoặc Anaconda Prompt, điều hướng đến thư mục gốc của dự án (`your_project_name/`) và chạy các lệnh sau:

```bash
# Tạo môi trường Conda mới từ file environment.yml
```shell
conda env create -f environment.yml
```
# Kích hoạt môi trường
```shell
conda activate phone_price_env 
```

Chạy API cục bộ
# Đảm bảo bạn đang ở thư mục gốc của dự án

---

## 🐳 Run with Docker Compose

### 1. Build and start services
```bash
docker compose up --build
```
### 2. Access the services 
| Service   | URL                                            |
| --------- | ---------------------------------------------- |
| FastAPI   | [http://localhost:8000](http://localhost:8000) |
| MLflow UI | [http://localhost:5000](http://localhost:5000) |

# test webhook
