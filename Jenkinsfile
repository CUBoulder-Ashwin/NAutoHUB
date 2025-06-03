pipeline {
    agent any

    environment {
        PROJECT_ROOT = "${env.WORKSPACE}"       // Assuming Jenkinsfile is in project root
        VIRTUAL_ENV = "${PROJECT_ROOT}/pilot-config/venv"
    }

    options {
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(numToKeepStr: '1'))
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "📥 Checking out source code..."
                checkout scm
            }
        }

        stage('Python Linting') {
            steps {
                echo "🔍 Linting Python files..."
                sh """
                . ${VIRTUAL_ENV}/bin/activate
                flake8 ${PROJECT_ROOT}/NSOT/python-files/ --max-line-length=150
                """
            }
        }

        stage('YAML Linting') {
            steps {
                echo "📄 Linting YAML files..."
                sh """
                . ${VIRTUAL_ENV}/bin/activate
                find ${PROJECT_ROOT} -path "*/venv" -prune -o -path "*/clab-Lab_AdvNet*" -prune -o \\( -name "*.yml" -o -name "*.yaml" \\) -print | xargs yamllint -d "{rules: {document-start: disable, truthy: disable}}"
                """
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "🧪 Running Unit Tests..."
                sh """
                . ${VIRTUAL_ENV}/bin/activate
                python3 -m unittest discover -s ${PROJECT_ROOT}/NSOT/python-files -p "test_suite.py"
                """
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