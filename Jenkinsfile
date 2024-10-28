pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "/home/student/Downloads/Advanced_Netman/CUBoulder-Ashwin/NSOT/GUI/flask_app/venv"
        PIP_CACHE_DIR = "${HOME}/.cache/pip" // Optional: reuse pip cache
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('YAML Validation') {
            steps {
                script {
                    sh '''
                    . ${VIRTUAL_ENV}/bin/activate
                    for file in $(find NSOT/templates -name "*.yml" -o -name "*.yaml"); do
                        echo "Validating $file"
                        python3 -c "import yaml, sys; yaml.safe_load(open('$file'))" || exit 1
                    done
                    '''
                }
            }
        }

        stage('Python Linting') {
            steps {
                sh '''
                . ${VIRTUAL_ENV}/bin/activate
                echo "Linting Python files in NSOT/python-files"
                flake8 NSOT/python-files/ || exit 1
                '''
            }
        }

        stage('Configuration Checks') {
            steps {
                script {
                    if (!fileExists('NSOT/configs/config.cfg')) {
                        error "Configuration file missing: NSOT/configs/config.cfg"
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
