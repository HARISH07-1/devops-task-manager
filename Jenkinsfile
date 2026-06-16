pipeline {
    agent any

    environment {
        IMAGE_NAME = "task-manager"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Checkout Source') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                echo 'Checking Docker installation...'
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('List Docker Images') {
            steps {
                echo 'Listing Docker images...'
                bat 'docker images'
            }
        }
    }

    post {

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check console output.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
