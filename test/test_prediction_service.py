# UNIT TEST cho PredictionService trực tiếp
import pytest
import pandas as pd
from app.prediction_service import PredictionService

def test_prediction_service_preprocess():
    service = PredictionService()

    raw_input = {
        "Model Name": "Galaxy S23 Ultra 512GB",
        "Company Name": "Samsung",
        "Launched Year": "2023",
        "Mobile Weight": "234g",
        "RAM": "12GB",
        "Front Camera": "40MP",
        "Back Camera": "200MP+12MP+10MP+10MP",
        "Battery Capacity": "5000mAh",
        "Screen Size": "6.8inches",
        "Processor": "Snapdragon 8 Gen 2",
        "Country": "Korea"
    }

    processed_df = service.preprocess_data(raw_input)

    # Kiểm tra số cột đúng bằng số cột đặc trưng đã train
    assert processed_df.shape[1] == len(service.trained_feature_columns)
    # Kiểm tra không có giá trị null
    assert not processed_df.isnull().values.any()

def test_prediction_service_predict():
    service = PredictionService()

    raw_input = {
        "Model Name": "Galaxy S23 Ultra 512GB",
        "Company Name": "Samsung",
        "Launched Year": "2023",
        "Mobile Weight": "234g",
        "RAM": "12GB",
        "Front Camera": "40MP",
        "Back Camera": "200MP+12MP+10MP+10MP",
        "Battery Capacity": "5000mAh",
        "Screen Size": "6.8inches",
        "Processor": "Snapdragon 8 Gen 2",
        "Country": "Korea"
    }

    predicted_price = service.predict_new_phone_price(raw_input)

    assert isinstance(predicted_price, float)
    assert predicted_price > 0

