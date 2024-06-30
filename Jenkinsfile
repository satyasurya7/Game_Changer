pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Example steps
                echo 'Building...'
            }
        }

        stage('Test') {
            steps {
                // Example steps
                echo 'Testing...'
            }
        }

        stage('Deploy') {
            steps {
                // Change directory to where your FastAPI application is located
                dir('~/Game_Changer/') {
                    // Run uvicorn to start FastAPI application
                    sh 'uvicorn main:app --port 8400 &'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
