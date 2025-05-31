from fastapi import FastAPI
from app.routes import phone

app = FastAPI(
    title="API Dự đoán Giá Điện thoại",
    description="API này dự đoán giá điện thoại dựa trên các thông số kỹ thuật.",
    version="1.0.0"
)

# Include routes từ module phone
app.include_router(phone.router)

@app.get("/")
async def root():
    return {"message": "Chào mừng đến với API Dự đoán Giá Điện thoại!"}

