### ✅ MLOps Pipeline for Phone Price Prediction API

---

### 1. Develop

- [x] Cleaned & preprocessed dataset
- [x] Train model (LGBMRegressor) with log(price)
- [x] Save model: 
  - `best_lgbm_regressor.joblib`
  - `scaler.joblib`
  - `feature_columns.joblib`
- [x] Build FastAPI app with:
  - `/predict` endpoint
  - Pydantic schema
  - Input preprocessing

🆕 MLflow:
- [x] Log experiment details (params, metrics, model artifacts)
- [x] Set up MLflow Tracking URI (localhost or remote)
- [x] Set up experiment name: `PhonePrice-Inference`

---

### 🐳 2. Docker

- [x] Dockerize FastAPI app with production-ready Dockerfile
- [x] Include model artifacts in Docker image
- [x] Run container locally: `docker run -p 8000:8000 phone-price-api`
- [x] Validate `/docs` and `/predict`

🆕 MLflow:
- [x] Ensure MLflow runs inside container (or connect to external MLflow Tracking Server)

---

### ☁️ 3. Infrastructure (GCP + IaC)

- [x] Use Terraform to provision:
  - GKE Cluster
  - Artifact Registry
  - GCS Bucket (for MLflow artifacts)
  - GCE VM (Jenkins host)
  - Firewall rules (port 8000, 5000, etc.)
- [x] Ansible to install Docker + dependencies (Jenkins VM)
- [x] Deploy MLflow & FastAPI to GKE via Helm

---

### 🔁 4. CI/CD

- [ ] Jenkins Pipeline or GitHub Actions:
  - [ ] Linting, Testing
  - [ ] Docker build & push to Artifact Registry
  - [ ] Helm deploy to GKE
- [ ] Trigger on push to `main` or via release tags

---

### 📊 5. Monitoring & Logging

- [ ] Prometheus + Grafana (via Helm):
  - [ ] Monitor FastAPI & MLflow pods
  - [ ] Basic request metrics, latency, error rate
- [ ] Logging:
  - [ ] GCP Logging (Cloud Logging)
  - [ ] Custom logging format (optional)

---

### 🎯 6. MLflow Integration (Experiment Tracking)

- [x] Log model training parameters (learning_rate, n_estimators, etc.)
- [x] Log metrics (MAE, RMSE)
- [x] Log model artifacts (joblib files)
- [x] Track inference events (request time, prediction result)
- [ ] (Optional) Register model to MLflow Model Registry
- [ ] (Optional) Serve model via `mlflow models serve`

---

✅ **Status**: Deployed FastAPI + MLflow on GCP with Terraform & Helm  
🔜 **Next**: Set up CI/CD (Jenkins or GitHub Actions), Monitoring & Logging

