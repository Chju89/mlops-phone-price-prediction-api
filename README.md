# 📦 MLOps - Phone Price Prediction API

> Dự án xây dựng hệ thống MLOps End-to-End sử dụng FastAPI, MLflow, Docker, Jenkins, Terraform, Helm, Ansible và được triển khai trên Google Cloud Platform (GCP).

---

## 📍 Mục tiêu dự án

Xây dựng pipeline MLOps hoàn chỉnh bao gồm:

* Triển khai hạ tầng GCP bằng Terraform
* Cài đặt Jenkins CI/CD bằng Ansible
* Viết pipeline build/test/deploy với Jenkins
* Deploy FastAPI và MLflow lên GKE bằng Helm
* Tích hợp Prometheus + Grafana giám sát FastAPI

---

## 🧰 Các thành phần chính

| Thành phần               | Mô tả                                                    |
| ------------------------ | -------------------------------------------------------- |
| **FastAPI**              | API dự đoán giá điện thoại từ input người dùng           |
| **MLflow**               | Quản lý training, log model, model registry              |
| **Jenkins**              | CI/CD pipeline: build image, deploy Helm chart           |
| **Terraform**            | Tạo hạ tầng GCP: GKE, Artifact Registry, GCS, VM Jenkins |
| **Ansible**              | Cài Docker, Jenkins, Helm, kubectl lên VM Jenkins        |
| **Helm**                 | Deploy FastAPI/MLflow lên GKE theo chart                 |
| **Prometheus + Grafana** | Thu thập metric từ API, visualize dashboard              |

---

## 🚀 Pipeline CI/CD (Jenkins)

**CI:**

* Lint code với `pre-commit`: Black, Ruff, Pytest
* Build Docker image cho FastAPI / MLflow
* Push image lên Artifact Registry

**CD:**

* Deploy lại lên GKE bằng Helm Chart với image mới nhất

---

## 📊 Monitoring

* FastAPI cung cấp `/metrics` (Prometheus format)
* Prometheus scrape metrics
* Grafana hiển thị:

  * Số lượng request
  * Thời gian phản hồi
  * RAM/CPU pod FastAPI sử dụng

---

## 🔐 Bảo mật & Quản lý Secrets

* Service Account JSON quản lý truy cập GCP (Artifact, GKE...)
* SSH key riêng cho VM Jenkins
* Các file nhạy cảm được ignore trong `.gitignore`

---

## 🔮 Cáu trúc thư mục repo

```
.
├── ansible/                # Cài Jenkins, Docker qua Ansible
│   ├── playbook.yml
│   ├── inventory.ini
│   └── roles/
│       ├── docker/
│       └── jenkins/
├── app/                   # FastAPI app code
│   ├── main.py
│   ├── routes/
│   ├── models/
│   └── services/
├── models/                # Mô hình ML: joblib files
├── helm/                  # Helm chart triển khai FastAPI/MLflow
│   ├── fastapi/
│   └── mlflow/
├── terraform/             # IaC: GKE, Artifact Registry, VM Jenkins, GCS
│   ├── *.tf
│   └── scripts/install_jenkins.sh
├── Dockerfile             # FastAPI
├── Dockerfile.mlflow      # MLflow
├── Jenkinsfile            # Jenkins pipeline
├── requirements/          # Python requirements chia theo service
├── environment.yml        # Conda env cho local
├── test/                  # Unit test FastAPI
├── notebook/              # Notebook khối tạo huấn luyện model
└── README.md
```

---

## ✨ Hướng dẫn triển khai

```bash
# 1. Tạo hạ tầng trên GCP
cd terraform/
terraform init && terraform apply

# 2. Cài Jenkins bằng Ansible
cd ansible/
ansible-playbook -i inventory.ini playbook.yml

# 3. Truy cập Jenkins: http://<VM-IP>:8080
# Tạo pipeline với Jenkinsfile trong repo

# 4. Trigger pipeline:
# Build image → Push Artifact Registry → Deploy Helm lên GKE

# 5. Truy cập:
# FastAPI: http://<LoadBalancer-IP>/docs
# MLflow UI: http://<LoadBalancer-IP-mlflow>
# Grafana: http://<LoadBalancer-IP-grafana>
```

---

## 🔬 Kết quả mô hình

* Dữ liệu: Tập giá điện thoại (RAM, camera, bộ nhớ...)
* Model: LGBM Regressor
* Đã scale + lưu model, scaler, features với joblib


---

## ✅ Tính năng nổi bật

* ✅ Triển khai hạ tầng toàn bộ bằng Terraform
* ✅ CI/CD tự động hoàn toàn với Jenkins
* ✅ Monitoring bằng Prometheus + Grafana
* ✅ Helm chart hoá việc deploy
* ✅ Quản lý code chuẩn với pre-commit (black, ruff, pytest)

---

## 📲 Liên hệ

> **Nguyễn Quang Triều**
> 📧 Email: \[email cá nhân]
> 👉 LinkedIn: \[link LinkedIn]
> 📂 CV: \[link Google Drive CV]

