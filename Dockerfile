# Dockerfile

# 1. Chọn image Python base nhẹ (bạn dùng Python 3.9)
FROM python:3.9-slim

# 2. Set thư mục làm việc trong container
WORKDIR /app

# 3. Cài thêm Libgomp1 để fix lỗi thiếu thư viện cho LightGBM
RUN apt-get update && apt-get install -y libgomp1 curl && rm -rf /var/lib/apt/lists/*

# 4. Copy file requirements.txt vào container
COPY requirements/fastapi.txt requirements.txt

# 5. Cài đặt các thư viện Python từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy toàn bộ mã nguồn vào container
COPY ./app ./app

# 7. Copy thư mục models chứa file model
COPY ./models ./models

# 8. Expose cổng ứng dụng (uvicorn mặc định là 8000)
EXPOSE 8000

# 9. Command chạy app khi container start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

