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
                    def python3-pep8_result = sh(script: 'pep8 mainClick.py', returnStatus: true)
                    if (python3-pep8_result != 0) {
                        error('PEP8 check failed. Please fix the formatting issues.')
                    }
                }
            }
        }
    }
}
