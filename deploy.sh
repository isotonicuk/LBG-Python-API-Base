#!/bin/bash
#specifies what utility should be used so in this case it would be bash. 
set -e
# Function to modify the application
modify_app() {
    echo "Modifying the application..."
    sleep 3
    export PORT=5001
    echo "Modifications done. Port is now set to $PORT"
}
# Function to run the Docker container
run_docker() {
    echo "Running Docker container..."
    sleep 3
    docker network create test-net || true
    docker run -d -p 80:$PORT -e PORT=$PORT --network test-net --name lbg-test $DOCKER_CREDS_USR/$DOCKER_IMAGE
    docker run -e PORT=$PORT --network test-net -v $(pwd):/app python:latest sh -c "pip install -r /app/requirements.txt; python /app/lbg.test.py"
}

echo "Deploying"
run_docker
echo "Successfully Deployed"
