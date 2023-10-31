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
               echo "ejecutando pruebas" // Ejecutar pruebas de Python utilizando unittest
                sh 'python -m unittest tests.py'
            }
        }

        stage('Publicar Resultados') {
            steps {
               echo "result" // Opcional: Publicar informes de pruebas o resultados
            }
        }
    }

    post {
        success {
            echo "aun nada"// Acciones posteriores si las pruebas son exitosas
        }
        failure {
           echo "aun nada" // Acciones posteriores si las pruebas fallan
        }
    }
}
