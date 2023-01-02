pipeline {
    agent none
    environment {
        DOCKER_IMAGE_PYTHON = 'python:3.10.9-alpine3.17'
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image '${DOCKER_IMAGE_PYTHON}'
                }
            }
            steps {
                sh 'python src/module_one.py'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image '${DOCKER_IMAGE_PYTHON}'
                }
            }
            steps {
                sh 'pip -m install pytest'
                sh 'pytest --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}