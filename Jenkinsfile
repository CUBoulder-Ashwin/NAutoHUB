pipeline {
    agent any
    environment {
        PROJECT_ROOT = "/home/student/Desktop/Advanced-Netman"
        VIRTUAL_ENV = "${PROJECT_ROOT}/venv"  // Adjust this to your actual venv path if needed
        PIP_CACHE_DIR = "${HOME}/.cache/pip"
    }

    options {
    buildDiscarder(logRotator(numToKeepStr: '1'))
}

    stages {

        stage('Python Linting') {
            steps {
                script {
                    def lintResult = sh(
                        script: """
                        echo "Linting Python files in NSOT/python-files"
                        . ${VIRTUAL_ENV}/bin/activate
                        flake8 ${PROJECT_ROOT}/NSOT/python-files/
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
                    echo "Linting YAML files in NSOT directory, excluding /venv and clab-Lab_AdvNet directories"
                    def yamlLintResult = sh(
                        script: """
                        . ${VIRTUAL_ENV}/bin/activate
                        find ${PROJECT_ROOT} -path "*/venv" -prune -o -path "*/clab-Lab_AdvNet*" -prune -o \\( -name "*.yml" -o -name "*.yaml" \\) -print | xargs yamllint -d "{rules: {document-start: disable, truthy: disable}}"
                        """,
                        returnStatus: true
                    )
                    if (yamlLintResult != 0) {
                        echo "YAML Linting encountered warnings or issues. If no response is seen here, this is probably a document-start or truthy warning, which is being ignored."
                        currentBuild.result = 'UNSTABLE'
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
                        python3 -m unittest discover -s ${PROJECT_ROOT}/NSOT/python-files -p "test_suite.py"
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
