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
                git url: 'git@github.com:Chju89/mlops-phone-price-prediction-api.git',
                    branch: 'main',
                    credentialsId: 'github-ssh-key'

                // Copy service account JSON key từ Jenkins credentials về workspace
                sh 'cp ~/gcp-sa-key.json $GOOGLE_APPLICATION_CREDENTIALS'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install -r requirements/fastapi.txt
                pip install black ruff pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                echo "🔍 Running black and ruff..."
                black --check . || true
                ruff . || true
                '''
            }
        }

        stage('Unit Test') {
            steps {
                sh '''
                echo "🧪 Running unit tests with MLFLOW disabled..."
                export DISABLE_MLFLOW=1
                PYTHONPATH=$PWD pytest test/
                '''
            }
        }

        stage('Docker Build & Push') {
            steps {
                sh '''
                echo "🔐 Authenticating with Google Cloud..."
                gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                gcloud auth configure-docker $REGION-docker.pkg.dev

                echo "🐳 Building Docker image..."
                docker build -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE_NAME:$IMAGE_TAG -f Dockerfile .

                echo "🚀 Pushing Docker image to Artifact Registry..."
                docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy to GKE') {
            steps {
                sh '''
                echo "🔄 Connecting to regional GKE cluster..."
                gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                gcloud container clusters get-credentials $GKE_CLUSTER --region $REGION --project $PROJECT_ID

                echo "📦 Deploying FastAPI using Helm..."
                helm upgrade --install fastapi ./helm/fastapi \
                  --set image.repository=$REGION-docker.pkg.dev/$PROJECT_ID/$REPO/$IMAGE_NAME \
                  --set image.tag=$IMAGE_TAG
                '''
            }
        }

        stage('Post-deploy Test') {
            steps {
                sh '''
                echo "⏳ Waiting for external IP..."
                sleep 30

                IP=$(kubectl get svc fastapi-fastapi -n default -o jsonpath="{.status.loadBalancer.ingress[0].ip}")
                echo "🌐 External IP: $IP"

                echo "🚀 Sending test request to /predict"
                curl -X POST http://$IP/predict \
                    -H "Content-Type: application/json" \
                    -d '{"battery_power":800, "ram":1000, "px_height":1000, "px_width":800, "mobile_wt":180, "int_memory":32, "dual_sim":1, "touch_screen":1, "wifi":1}'
                '''
            }
        }
    }
}

