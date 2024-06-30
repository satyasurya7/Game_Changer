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

        stage('Test') {
            steps {
                // Example: Run tests (if needed)
                sh 'pytest'
                // Additional test steps as necessary
            }
        }

        stage('Deploy') {
            steps {
                // Example deployment command
                sh 'uvicorn main:app --port 8400 &'
                // Replace with your actual deployment command or script
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
