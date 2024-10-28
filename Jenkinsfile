pipeline {
    agent any

    environment {
        // Define any environment variables here if needed
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the repository
                checkout scm
            }
        }

        stage('YAML Validation') {
            steps {
                script {
                    // Validate YAML files specifically in the NSOT/templates directory
                    sh '''
                    for file in $(find NSOT/templates -name "*.yml" -o -name "*.yaml"); do
                        echo "Validating $file"
                        python -c "import yaml, sys; yaml.safe_load(open('$file'))" || exit 1
                    done
                    '''
                }
            }
        }

        stage('Python Linting') {
            steps {
                // Lint Python files specifically in the NSOT/python-files directory
                sh '''
                echo "Linting Python files in NSOT/python-files"
                flake8 NSOT/python-files/ || exit 1
                '''
            }
        }

        stage('Configuration Checks') {
            steps {
                script {
                    // Check for specific configuration files in the NSOT/configs directory
                    def configFiles = ['config.cfg'] // Add any other specific filenames if needed
                    
                    for (configFile in configFiles) {
                        def filePath = "NSOT/configs/${configFile}"
                        if (!fileExists(filePath)) {
                            error "Configuration file missing: ${filePath}"
                        }
                    }
                    
                    echo "All required configuration files are present."
                }
            }
        }

        stage('Golden Configs Check') {
            steps {
                script {
                    // Check if the NSOT/golden_configs directory exists and has required files
                    def goldenConfigFiles = findFiles(glob: 'NSOT/golden_configs/*.cfg')
                    
                    if (goldenConfigFiles.length == 0) {
                        error "No golden configuration files found in NSOT/golden_configs"
                    }

                    echo "Golden configuration files are present."
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace'
            deleteDir() // Clean up workspace
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the console output for details.'
        }
    }
}
