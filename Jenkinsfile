pipeline {
    agent any

    environment {
        IMAGE_NAME = "harishhh07/task-manager"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }
    }

    post {
        success {
            echo 'Docker image pushed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
