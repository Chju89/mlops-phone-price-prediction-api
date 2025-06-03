### Terraform Infrastructure Setup for MLOps Pipeline
This terraform/ directory contains Infrastructure as Code (IaC) configuration to provision all necessary GCP resources for deploying a production-ready MLOps pipeline.

### Resources Provisioned
| Resource              | Description                                    |
| --------------------- | ---------------------------------------------- |
| **GKE Cluster**       | Deploy FastAPI & MLflow using Helm             |
| **Artifact Registry** | Store Docker images built from FastAPI/MLflow  |
| **GCS Bucket**        | Store MLflow artifacts (models, metrics, logs) |
| **Jenkins VM (GCE)**  | CI/CD orchestration using Jenkins              |
| **Firewall Rules**    | Open ports: 8080 (Jenkins), 5000 (MLflow)      |

### Prerequisites
 - Terraform ≥ 1.3
 - Google Cloud SDK (gcloud)
 - A GCP project with billing enabled
 - Enable the following APIs:
    . Compute Engine API
    . Kubernetes Engine API
    . Artifact Registry API
    . Cloud Storage API

Your GCP account is authenticated:
```bash
gcloud auth application-default login
```

### File Structure
terraform/
├── main.tf                # Main resource definitions
├── provider.tf            # GCP provider configuration
├── variables.tf           # Input variables
├── terraform.tfvars       # Your project-specific values
├── outputs.tf             # Outputs like IPs and URLs
├── scripts/
│   └── install_jenkins.sh # Jenkins auto-install script


### Usage
1. Initialize Terraform
```bash
cd terraform
```

2. Set your project ID
Edit terraform.tfvars:
```hcl
project_id = "your-gcp-project-id"
```

3. Apply to provision infrastructure
```bash
terraform apply
```
Confirm when prompted with yes.


### Access Services After Deply
 - Jenkins:
   http://<jenkins_vm_ip>:8080
   Default password:
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

 - MLflow UI:
   http://<jenkins_vm_ip>:5000

### Next Steps
 - Push Docker images to Artifact Registry.
 - Use Jenkins to trigger CI/CD:
    . Build & push Docker images
    . Deploy via Helm to GKE
 - Configure Helm charts for FastAPI and MLflow
 - Set up Prometheus + Grafana for monitoring


### Output:
artifact_registry_repo = "mlops-repo"
bucket_name = "mle-course-454508-mlflow-bucket"
gke_cluster_name = "mlops-cluster"
jenkins_vm_ip = "34.30.166.93"

