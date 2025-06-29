# 🚀 Helm Charts - FastAPI & MLflow

Thư mục này chứa Helm charts để triển khai:

- FastAPI: phục vụ API dự đoán
- MLflow: UI theo dõi, quản lý mô hình ML

## Cấu trúc
```
helm/
├── fastapi/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
└── mlflow/
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
```

## Deploy bằng Helm
```bash
helm upgrade --install fastapi ./fastapi
helm upgrade --install mlflow ./mlflow
```
