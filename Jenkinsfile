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
    }
        stages {
        stage('Build step') {
            steps {
                sh "sh build.sh"
            }
        }
    }
        stages {
        stage('Deploy step') {
            steps {
                sh "sh deploy.sh"
            }
        }
    }
}