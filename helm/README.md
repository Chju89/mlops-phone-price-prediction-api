
# Phone Price Prediction API - Deployment on GKE

This repository contains Helm charts to deploy the Phone Price Prediction API (FastAPI) and MLflow tracking server on Google Kubernetes Engine (GKE).

---

## Prerequisites

- Google Cloud project with billing enabled
- GKE cluster created and `kubectl` configured to access it
- Google Artifact Registry with Docker images pushed:
  - `phone-price-api-fastapi`
  - `phone-price-api-mlflow`
- Helm installed locally ([Install Helm](https://helm.sh/docs/intro/install/))

---

## Deployment Steps

### 1. Connect to your GKE cluster

```bash
gcloud container clusters get-credentials <CLUSTER_NAME> --zone <ZONE> --project <PROJECT_ID>
```

---

### 2. Deploy MLflow tracking server

MLflow is used to track model experiments and logs.

```bash
helm install mlflow ./helm/mlflow --namespace mlflow --create-namespace
```

Check pod status:

```bash
kubectl get pods -n mlflow
```

---

### 3. Deploy FastAPI application

```bash
helm install fastapi ./helm/fastapi --namespace fastapi --create-namespace
```

Check pod status:

```bash
kubectl get pods -n fastapi
```

---

### 4. Access services

If you don't have LoadBalancer or Ingress configured, you can use port-forwarding:

- MLflow UI:

```bash
kubectl port-forward svc/mlflow 5000:5000 -n mlflow
```

Access MLflow at: [http://localhost:5000](http://localhost:5000)

- FastAPI API:

```bash
kubectl port-forward svc/fastapi 8000:8000 -n fastapi
```

Access FastAPI docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 5. Test FastAPI predict endpoint

Use curl or Postman to test prediction API:

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "feature1": value1,
  "feature2": value2,
  ...
}'
```

Replace the JSON body with your actual input features.

---

## Notes

- This setup uses minimal resource configuration for free-tier GKE clusters.
- For production, consider adding Persistent Volumes, LoadBalancer or Ingress, and securing services.
- You can automate build and deployment with Jenkins or GitHub Actions.

---

## Troubleshooting

- Check pod logs:

```bash
kubectl logs -l app=mlflow -n mlflow
kubectl logs -l app=fastapi -n fastapi
```

- Verify Helm releases:

```bash
helm list -n mlflow
helm list -n fastapi
```

---

Feel free to open issues or contribute!
