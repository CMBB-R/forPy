pipeline {
    agent any
    stages {
        stage('InstallPy') {
            steps {
                sh 'pyenv install 3.8.12'
            }
        }
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
