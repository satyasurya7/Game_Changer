pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Create a virtual environment and activate it
                script {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                // Example: Run tests (adjust as per your testing framework)
                script {
                    sh '''
                        source venv/bin/activate
                        pytest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                // Example deployment command
                script {
                    sh '''
                        source venv/bin/activate
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
