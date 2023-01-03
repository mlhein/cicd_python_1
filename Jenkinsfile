pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.10.9-alpine3.17'
                }
            }
            steps {
                sh 'python -m compileall ./src/'
                sh 'python -m compileall ./test/'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.10.9-alpine3.17'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m pip install --user requirements.txt'
                    sh 'python -m pytest --junit-xml test-reports/results.xml'
                }
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}