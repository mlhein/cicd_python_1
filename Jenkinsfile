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
    }
}