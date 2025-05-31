from fastapi import APIRouter, HTTPException, Body
from app.models.phone_schema import PhoneData
from app.services.prediction_service import PredictionService

router = APIRouter()

prediction_service = PredictionService()

@router.post("/predict")
async def predict_phone_price(
    phone_data: PhoneData = Body(
        ...,
        examples={
            "default": {
                "summary": "Ví dụ điện thoại Samsung",
                "value": {
                    "Company Name": "Samsung",
                    "Model Name": "Galaxy S21 5G 128GB",
                    "Processor": "Qualcomm Snapdragon 888",
                    "Launched Year": 2021,
                    "Mobile Weight": "169g",
                    "RAM": "8GB",
                    "Front Camera": "10MP",
                    "Back Camera": "12MP+64MP+12MP",
                    "Battery Capacity": "4000mAh",
                    "Screen Size": "6.2inches",
                    "Country": "USA"
                }
            }
        }
    )
):
    if prediction_service.best_lgbm_model is None:
        raise HTTPException(status_code=500, detail="Mô hình dự đoán chưa sẵn sàng. Vui lòng kiểm tra log server.")

    try:
        raw_input_data = phone_data.model_dump(by_alias=True)
        predicted_price = prediction_service.predict_new_phone_price(raw_input_data)
        return {"predicted_price_USD": round(predicted_price, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Đã xảy ra lỗi trong quá trình dự đoán: {e}")

