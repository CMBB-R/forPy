pipeline {
    agent any
    stages {
        stage('Install Python') {
            steps {
                script {
                    // Set the desired Python version
                    def pythonVersion = '3.8.12' // Replace with your desired version
                    def pythonHome = tool name: "Python-${pythonVersion}", type: 'hudson.plugins.python.PythonInstallation'
                    env.PATH = "${pythonHome}/bin:${env.PATH}"
                }
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
