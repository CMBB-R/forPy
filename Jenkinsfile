pipeline {
    agent any
    stages {
stage('Install Dependencies') {
    steps {
        sh 'python3 -m pip install click'
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
