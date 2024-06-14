pipeline { 
    agent any
    environment {
        DOCKER_IMAGE = "lbg"
        PORT = "9000"
        DOCKER_CREDS = credentials('dockerhub')
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
        stage('PUsh to Docker Hub') {
            steps {
                sh '''
                docker login -u $DOCKER_CREDS_USR -p $$DOCKER_CREDS_PSW
                docker push $DOCKER_CREDS_USR/$DOCKER_IMAGE
                docker logout
                '''
            }
        }
    }
}