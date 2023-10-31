pipeline {
    agent any

    stages {
    
        stage('Configurar Entorno') {
            steps {
                // Instalar Python y crear un entorno virtual
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'

                // Instalar dependencias
                sh 'pip install -r requirements.txt'  // Si tienes un archivo de requisitos
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                // Ejecutar pruebas de Python utilizando unittest
                sh 'python -m unittest tests.py'
            }
        }

        stage('Publicar Resultados') {
            steps {
                // Opcional: Publicar informes de pruebas o resultados
            }
        }
    }

    post {
        success {
            // Acciones posteriores si las pruebas son exitosas
        }
        failure {
            // Acciones posteriores si las pruebas fallan
        }
    }
}
