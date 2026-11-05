pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                sh 'docker compose config --quiet'
            }
        }

        stage('Build Microservices') {
            steps {
                sh 'docker compose build user-service product-service order-service'
            }
        }

        stage('Tag Docker Images') {
            steps {
                sh '''
                    docker tag user-service:1.0 user-service:${BUILD_NUMBER}
                    docker tag product-service:1.0 product-service:${BUILD_NUMBER}
                    docker tag order-service:1.0 order-service:${BUILD_NUMBER}
                '''
            }
        }

        stage('Verify Docker Images') {
            steps {
                sh '''
                    docker image inspect user-service:${BUILD_NUMBER}
                    docker image inspect product-service:${BUILD_NUMBER}
                    docker image inspect order-service:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Check the stage logs.'
        }
    }
}
