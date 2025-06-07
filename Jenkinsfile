pipeline {
  agent any

  environment {
    PROJECT_ID = 'your-gcp-project-id'
    IMAGE_NAME = "gcr.io/${PROJECT_ID}/phone-price-api"
    IMAGE_TAG = "latest"
    CHART_PATH = "charts/fastapi"
    RELEASE_NAME = "fastapi-app"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Lint & Test') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'flake8 app/'
        sh 'pytest tests/'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
      }
    }

    stage('Push to GCR') {
      steps {
        withCredentials([file(credentialsId: 'gcp-service-account-key', variable: 'GCP_KEY')]) {
          sh '''
            gcloud auth activate-service-account --key-file=$GCP_KEY
            gcloud auth configure-docker
            docker push ${IMAGE_NAME}:${IMAGE_TAG}
          '''
        }
      }
    }

    stage('Deploy to GKE') {
      steps {
        withCredentials([file(credentialsId: 'gcp-service-account-key', variable: 'GCP_KEY')]) {
          sh '''
            gcloud auth activate-service-account --key-file=$GCP_KEY
            gcloud container clusters get-credentials mlops-cluster --zone YOUR_ZONE --project $PROJECT_ID
            helm upgrade --install ${RELEASE_NAME} ${CHART_PATH} --set image.tag=${IMAGE_TAG}
          '''
        }
      }
    }
  }
}

