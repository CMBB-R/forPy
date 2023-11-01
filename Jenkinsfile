pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('mainClick') {
            steps {
                sh 'python3 mainClick.py'
            }
        }
    }
}
