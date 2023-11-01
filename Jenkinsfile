pipeline {
    agent any
    stages {
     
        stage('versionPy') {
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
