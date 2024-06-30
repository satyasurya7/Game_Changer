pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Create and activate a virtual environment
                script {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate  # Use dot (.) instead of source
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Activate virtual environment and run tests
                    sh '''
                        . venv/bin/activate
                        pytest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Activate virtual environment and deploy
                    sh '''
                        . venv/bin/activate
                        uvicorn main:app --port 8400 &
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
            // Add post-success actions if needed
        }
        failure {
            echo 'Pipeline failed!'
            // Add post-failure actions if needed
        }
    }
}
