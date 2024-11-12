pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "/home/student/Downloads/Advanced_Netman/CUBoulder-Ashwin/NSOT/GUI/flask_app/venv"
        PIP_CACHE_DIR = "${HOME}/.cache/pip"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing yamllint in virtual environment"
                    sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    pip install yamllint
                    """
                }
            }
        }

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

        stage('YAML Linting') {
            steps {
                script {
                    echo "Linting YAML files in NSOT directory, excluding /venv"
                    def yamlLintResult = sh(
                        script: """
                        . ${VIRTUAL_ENV}/bin/activate
                        find . -path "*/venv" -prune -o \\( -name "*.yml" -o -name "*.yaml" \\) -print | xargs yamllint
                        """,
                        returnStatus: true
                    )
                    if (yamlLintResult != 0) {
                        echo "YAML Linting encountered issues. Consider fixing YAML syntax."
                        currentBuild.result = 'UNSTABLE'  // Optional: Mark as unstable if linting fails
                    } else {
                        echo "YAML Linting passed successfully."
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
