pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-api-local:latest .'
            }
        }
        stage('Lint') {
            steps {
                sh 'docker run --rm -v $WORKSPACE/app:/app flask-api-local:latest flake8 /app'
            }
        }
        stage('Deploy to Remote') {
            steps {
                withCredentials([
                    string(credentialsId: 'REMOTE_USER_ID', variable: 'REMOTE_USER'),
                    string(credentialsId: 'REMOTE_HOST_ID', variable: 'REMOTE_HOST'),
                    string(credentialsId: 'REMOTE_PATH_ID', variable: 'REMOTE_PATH')
                ]) {
                    sshagent(['36115e99-9064-4a1e-acd5-8d6ee2778db9']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST} '
                                set -e
                                if [ ! -d ${REMOTE_PATH} ]; then
                                    git clone https://github.com/KapitanTito/flask-api-finaltest.git ${REMOTE_PATH}
                                fi
                                cd ${REMOTE_PATH}
                                git pull
                                docker-compose down || true
                                docker-compose up -d --build
                            '
                        """
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}