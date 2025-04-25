pipeline {
    agent any

    environment {
        PROJECT_ROOT = "${env.WORKSPACE}/pilot-config"
        VIRTUAL_ENV = "${PROJECT_ROOT}/venv"
        PIP_CACHE_DIR = "${HOME}/.cache/pip"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '1'))
    }

    stages {
        stage('Python Linting') {
            steps {
                script {
                    echo "🔍 Linting Python files..."
                    sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    flake8 ${PROJECT_ROOT}/../NSOT/python-files/
                    """
                }
            }
        }

        stage('YAML Linting') {
            steps {
                script {
                    echo "🔍 Linting YAML files (excluding venv & clab-Lab_AdvNet)"
                    sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    find ${env.WORKSPACE} -path "*/venv" -prune -o -path "*/clab-Lab_AdvNet*" -prune -o \\( -name "*.yml" -o -name "*.yaml" \\) -print | xargs yamllint -d "{rules: {document-start: disable, truthy: disable}}"
                    """
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    echo "🧪 Running Unit Tests..."
                    sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    python3 -m unittest discover -s ${env.WORKSPACE}/NSOT/python-files -p "test_suite.py"
                    """
                }
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace'
            deleteDir()
        }
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. Check the console output for details.'
        }
    }
}
