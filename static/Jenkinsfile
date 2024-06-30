pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Example: Install dependencies (if needed)
                sh 'pip install -r requirements.txt'
                // Additional build steps as necessary
            }
        }

        stage('Deploy') {
            steps {
                 {
                    // Run uvicorn to start FastAPI application
                    sh 'uvicorn main:app --port 8400 &'
                }
            }
        }
    }

    post {
        success {
            // Notification or other actions on success
        }
        failure {
            // Notification or other actions on failure
        }
    }
}
