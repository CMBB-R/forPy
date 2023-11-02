pipeline {
    agent any
    stages {
        stage('versionPy') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Check Format') {
            steps {
                script {
                    sh 'pycodestyle your_script.py'
                    }
                }
            }
        }
    }

