# ✅ Checklist - MLOps Project Quality

## 🌐 Repository Structure
- [x] Có cấu trúc thư mục rõ ràng (app/, helm/, terraform/, etc)
- [x] Có README.md đầy đủ
- [x] Có LICENSE & CONTRIBUTING.md

## 🚀 CI/CD
- [x] Có file Jenkinsfile
- [x] Jenkins hoạt động ổn định (build/test/deploy)
- [x] Có pre-commit: Black, Ruff, Pytest

## 📦 Docker & Helm
- [x] Dockerfile chia tách rõ FastAPI & MLflow
- [x] Helm chart deploy được lên GKE

## ☁️ GCP Infrastructure
- [x] Terraform tạo GKE, GCS, VM, Artifact Registry
- [x] Ansible cài Jenkins đầy đủ

## 📊 Monitoring
- [x] FastAPI expose `/metrics`
- [x] Prometheus scrape metrics
- [x] Grafana visualize (request, latency, error rate)

## 🧪 Testing
- [x] Có test trong thư mục `test/`
- [x] Test chạy qua Jenkins CI

## 🔒 Security
- [x] Secrets được `.gitignore`
- [x] Không push file nhạy cảm lên Git

