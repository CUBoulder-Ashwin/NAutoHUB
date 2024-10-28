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
                    // Validate the devices_config.yml file
                    def result = sh(
                        script: """
                        . ${VIRTUAL_ENV}/bin/activate
                        yaml_file="NSOT/templates/devices_config.yml"
                        if [ -f "$yaml_file" ]; then
                            echo "Validating $yaml_file"
                            python3 -c "import yaml, sys; yaml.safe_load(open('$yaml_file'))" || exit 1
                        else
                            echo "YAML file $yaml_file not found."
                            exit 1
                        fi
                        """,
                        returnStatus: true
                    )
                    if (result != 0) {
                        echo "YAML Validation failed for devices_config.yml, but proceeding to next stage."
                    } else {
                        echo "YAML Validation for devices_config.yml passed."
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
                    // List of required configuration files
                    def requiredFiles = ['R1.cfg', 'R2.cfg', 'R3.cfg', 'R4.cfg', 'S1.cfg', 'S2.cfg', 'S3.cfg', 'S4.cfg']
                    def missingFiles = []

                    // Check if each required file exists
                    requiredFiles.each { file ->
                        def filePath = "NSOT/configs/${file}"
                        if (!fileExists(filePath)) {
                            echo "Configuration file missing: ${filePath}"
                            missingFiles << file
                        } else {
                            echo "Found configuration file: ${filePath}"
                        }
                    }

                    // Log error if any files are missing
                    if (missingFiles) {
                        echo "The following configuration files are missing: ${missingFiles.join(', ')}"
                    } else {
                        echo "All required configuration files are present."
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
