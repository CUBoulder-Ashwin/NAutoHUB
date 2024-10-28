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

        stage('Auto-fix PEP8') {
            steps {
                script {
                    // Run autopep8 to fix PEP8 issues automatically
                    def result = sh(
                        script: """
                        . ${VIRTUAL_ENV}/bin/activate
                        autopep8 --in-place --aggressive --aggressive NSOT/python-files/*.py
                        """,
                        returnStatus: true
                    )
                    if (result != 0) {
                        echo "Auto-fix PEP8 encountered issues, but proceeding to next stage."
                    }
                }
            }
        }

        stage('YAML Validation') {
            steps {
                script {
                    // Validate YAML files
                    def result = sh(
                        script: """
                        . ${VIRTUAL_ENV}/bin/activate
                        for file in \$(find NSOT/templates -name "*.yml" -o -name "*.yaml"); do
                            echo "Validating \$file"
                            python3 -c "import yaml, sys; yaml.safe_load(open('\$file'))" || exit 1
                        done
                        """,
                        returnStatus: true
                    )
                    if (result != 0) {
                        echo "YAML Validation failed, but proceeding to next stage."
                    }
                }
            }
        }

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

        stage('Configuration Checks') {
            steps {
                script {
                    if (!fileExists('NSOT/configs/config.cfg')) {
                        echo "Configuration file missing: NSOT/configs/config.cfg"
                    } else {
                        echo "Configuration file check passed."
                    }
                }
            }
        }

        stage('Golden Configs Check') {
            steps {
                script {
                    // Verify presence of files in golden_configs
                    def files = findFiles(glob: 'NSOT/golden_configs/*.cfg')
                    if (files.length == 0) {
                        echo "No files found in NSOT/golden_configs/"
                    } else {
                        echo "Golden Configs Check passed. Found ${files.length} config files."
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
