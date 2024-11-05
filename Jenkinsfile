pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "/home/student/Downloads/Advanced_Netman/CUBoulder-Ashwin/NSOT/GUI/flask_app/venv"
        PIP_CACHE_DIR = "${HOME}/.cache/pip"
    }

    stages {
        stage('Python Linting') {
            steps {
                script {
                    def lintResult = sh(
                        script: """
                        echo "Linting Python files in NSOT/python-files"
                        . ${VIRTUAL_ENV}/bin/activate
                        flake8 NSOT/python-files/
                        """,
                    )
                    if (lintResult != null) {
                        echo "Python Linting encountered issues, but proceeding to next stage."
                    } else {
                        echo "Python Linting passed successfully."
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    echo "Running Unit Tests"
                    def testResult = sh(
                        script: """
                        . ${VIRTUAL_ENV}/bin/activate
                        python3 -m unittest discover -s NSOT/python-files -p "test_suite.py"
                        """,
                    )
                    if (testResult != null) {
                        echo "Unit tests encountered issues. Please check the logs."
                        currentBuild.result = 'UNSTABLE'
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
