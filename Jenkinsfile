pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Set up Python virtual environment
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'

                    // Install dependencies
                    sh 'pip install -r requirements.txt'

                    // Run tests
                    sh 'python -m unittest discover tests'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests passed. Ready for deployment!'
            // Add deployment steps here if needed
        }
        failure {
            echo 'Build or tests failed. Check the logs for details.'
        }
    }
}
