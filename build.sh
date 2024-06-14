#!/bin/bash
#specifies what utility should be used so in this case it would be bash. 
set -e
# Function to build the Docker image
build_docker() {
    echo "Building the Docker image..."
    sleep 3
    docker build -t $DOCKER_CREDS_USR/$DOCKER_IMAGE .
}
echo "Start Build Process"
build_docker
echo "Finished Build Process $DOCKER_CREDS_USR/$DOCKER_IMAGE"