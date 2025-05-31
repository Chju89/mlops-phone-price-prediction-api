# INTERGRATION TEST (using TestClient)
import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_predict_endpoint_success():
    sample_input = {
        "Model Name": "iPhone 14 Pro 256GB",
        "Company Name": "Apple",
        "Launched Year": "2022",
        "Mobile Weight": "210g",
        "RAM": "6GB",
        "Front Camera": "12MP",
        "Back Camera": "48MP+12MP+12MP",
        "Battery Capacity": "3200mAh",
        "Screen Size": "6.1inches",
        "Processor": "A16 Bionic",
        "Country": "USA"
    }

    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    result = response.json()
    assert "predicted_price" in result
    assert isinstance(result["predicted_price"], float)
    assert result["predicted_price"] > 0


def test_predict_endpoint_invalid_input():
    bad_input = {
        "Model Name": "Some Phone",
        "Company Name": "BrandX"
        # thiếu các trường bắt buộc khác
    }

    response = client.post("/predict", json=bad_input)
    assert response.status_code == 422  # Lỗi do thiếu field

