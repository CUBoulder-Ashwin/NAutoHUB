pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "/home/student/Downloads/Advanced_Netman/CUBoulder-Ashwin/NSOT/GUI/flask_app/venv"
        PIP_CACHE_DIR = "${HOME}/.cache/pip" // Optional: reuse pip cache
    }

    stages {
        stage('Python Linting') {
            steps {
                script {
                    def result = sh(
                        script: """
                        echo "Linting Python files in NSOT/python-files"
                        . ${VIRTUAL_ENV}/bin/activate
                        flake8 NSOT/python-files/
                        """,
                        returnStatus: true
                    )
                    if (result != 0) {
                        echo "Python Linting encountered issues, but proceeding to next stage."
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace'
            deleteDir()
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
