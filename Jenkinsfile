pipeline {
    agent any

    environment {
        PROD_PATH = "/var/jenkins_home/flask-api-prod"    // путь куда будем деплоить "прод"
        APP_PATH = "${env.WORKSPACE}"                // путь к текущему коду (workspace Jenkins)
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
                    sh 'docker build -t flask-api-local:latest .'
                }
            }
        }
        stage('Lint') {
            steps {
                script {
                    sh 'docker run --rm -v $WORKSPACE/app:/app flask-api-local:latest flake8 /app'
                }
            }
        }
        stage('Prepare Production Directory') {
            steps {
                script {
                    // —оздаЄм прод-папку если не существует
                    sh '''
                    mkdir -p ${PROD_PATH}
                    cp -rT ${APP_PATH} ${PROD_PATH}
                    '''
                }
            }
        }
        stage('Deploy (docker-compose up)') {
            steps {
                script {
                    // «апускаем (или перезапускаем) приложение на "прод" окружении
                    sh """
                    cd ${PROD_PATH}
                    docker-compose down || true
                    docker-compose up -d --build
                    """
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
