pipeline { 
    agent any
    environment {
        DOCKER_IMAGE = "lbg"
        PORT = "9000"
    }
    stages {
        stage('Cleanup step') {
            steps {
                sh "sh setup.sh"
            }
        }
        stage('Build step') {
            steps {
                sh "sh build.sh"
            }
        }
        stage('Deploy step') {
            steps {
                sh "sh deploy.sh"
            }
        }
    }
}