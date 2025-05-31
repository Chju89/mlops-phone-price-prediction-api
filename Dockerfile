# Dockerfile

# 1. Chọn image Python base nhẹ (bạn dùng Python 3.9)
FROM python:3.9-slim

# 2. Set thư mục làm việc trong container
WORKDIR /app

# 3. Copy file requirements.txt vào container
COPY requirements.txt .

# 4. Cài đặt các thư viện Python từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ mã nguồn vào container
COPY ./app ./app

# 6. Expose cổng ứng dụng (uvicorn mặc định là 8000)
EXPOSE 8000

# 7. Command chạy app khi container start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

