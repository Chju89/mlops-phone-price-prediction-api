# ☁️ Terraform - Hạ tầng GCP

Thư mục này dùng để tạo toàn bộ hạ tầng GCP bao gồm:

- GKE Cluster
- Artifact Registry
- GCS Bucket
- VM Jenkins
- Firewall rules

## Cấu trúc
```
terraform/
├── main.tf
├── variables.tf
├── outputs.tf
├── provider.tf
└── scripts/
    └── install_jenkins.sh
```

## Triển khai
```bash
terraform init
terraform apply
```
