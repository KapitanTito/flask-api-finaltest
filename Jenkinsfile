pipeline {
    agent any

    environment {
        REGISTRY = 'docker.io/yourdockerhubusername/flask-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER_IMAGE = "${REGISTRY}:${IMAGE_TAG}"
        SSH_USER = 'deployuser'
        SSH_HOST = 'your.server.ip.address'
        SSH_PATH = '/home/deployuser/flask-api'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Lint & Test') {
            steps {
                script {
                    // Если нужен flake8, иначе просто "echo No tests"
                    sh """
                        docker run --rm -v $PWD:/app -w /app python:3.10-slim sh -c "pip install flake8 && flake8 app/"
                    """
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${DOCKER_IMAGE}"
            }
        }

        stage('Deploy to Remote Server') {
            steps {
                sshagent(['jenkins-ssh-key']) {
                    // Останавливаем старый сервис, подтягиваем новый compose, поднимаем
                    sh """
                        ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SSH_HOST} '
                            set -e
                            cd ${SSH_PATH}
                            echo "Updating .env and docker-compose.yml if changed..."
                            git pull || true
                            sed -i "s|image: .*\$|image: ${DOCKER_IMAGE}|" docker-compose.yml
                            docker-compose pull
                            docker-compose down
                            docker-compose up -d
                        '
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            mail to: 'your-email@example.com',
                 subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Check Jenkins for details!"
        }
    }
}