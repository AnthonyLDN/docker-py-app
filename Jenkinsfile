node {
    def db, app

    stage('Clone Repository') {
        checkout scm
    }

    stage('Build Docker Images') {
        echo "Building database image."
        db = docker.build("py-app-db", "/var/jenkins_home/workspace/docker-pipeline/db")
    }
}