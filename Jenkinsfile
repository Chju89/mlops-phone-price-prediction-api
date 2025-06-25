pipeline {
    agent any

    environment {
        PROJECT_ID = 'mle-course-454508'
        IMAGE_NAME = 'phone-price-api-mlflow'
        IMAGE_TAG = 'latest'
        REGION = 'us-central1'
        REPO = 'mlops-repo'
        GKE_CLUSTER = 'mlops-cluster'
        GKE_ZONE = 'us-central1-a'
        GOOGLE_APPLICATION_CREDENTIALS = "${WORKSPACE}/gcp-sa-key.json"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone repo bằng SSH (đảm bảo đã tạo credential trong Jenkins)
                git url: 'git@github.com:Chju89/mlops-phone-price-prediction-api.git', credentialsId: 'github-ssh-key'

                // Copy file .json vào workspace
                sh 'cp ~/gcp-sa-key.json $GOOGLE_APPLICATION_CREDENTIALS'
            }
        }

        stage('Install Python Deps') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install black ruff pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                black --check .
                ruff .
                '''
            }
        }

        stage('Unit Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Docker Build & Push') {
            steps {
                sh '''
                gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                gcloud auth configure-docker $REGION-docker.pkg.dev

                docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE_NAME:$IMAGE_TAG -f Dockerfile .
                docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy to GKE') {
            steps {
                sh '''
                gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                gcloud container clusters get-credentials $GKE_CLUSTER --zone $GKE_ZONE --project $PROJECT_ID

                helm upgrade --install fastapi ./helm/fastapi \
                  --set image.repository=$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE_NAME \
                  --set image.tag=$IMAGE_TAG
                '''
            }
        }

        stage('Post-deploy Test') {
            steps {
                sh '''
                echo "⏳ Waiting for FastAPI service to get external IP..."
                sleep 30

                IP=$(kubectl get svc fastapi -o jsonpath="{.status.loadBalancer.ingress[0].ip}")
                echo "🌐 External IP: $IP"

                echo "🚀 Sending test request to /predict endpoint"
                curl -X POST http://$IP:8000/predict \
                     -H "Content-Type: application/json" \
                     -d '{"battery_power":800, "ram":1000, "px_height":1000, "px_width":800, "mobile_wt":180, "int_memory":32, "dual_sim":1, "touch_screen":1, "wifi":1}'
                '''
            }
        }
    }
}

