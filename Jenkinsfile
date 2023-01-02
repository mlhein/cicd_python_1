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
                sh 'python src/module_one.py'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.10.9-alpine3.17'
                }
            }
            steps {
                // withEnv(["HOME=${env.WORKSPACE}"]) {
                sh 'python -m pip install --user pytest'
                sh 'python -m pytest --junit-xml test-reports/results.xml'
                // }
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}