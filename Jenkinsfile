
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code fetched from GitHub'
            }
        }

        stage('Automated Tests') {
            steps {
                bat 'python -m unittest test_form.py -v'
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed. Check the console output.'
        }
    }
}
