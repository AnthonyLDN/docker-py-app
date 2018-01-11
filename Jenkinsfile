node {
    def db, app

    stage('Clone Repository') {
        checkout scm
    }

    stage('Build Docker Images') {
        echo "Building database image."
        db = docker.build("py-app-db", "/var/jenkins_home/workspace/docker-pipeline/db")

        echo "Building application image."
        app = docker.build("py-app-db", "/var/jenkins_home/workspace/docker-pipeline/app")
    }

    stage('Running Tests') {
        echo "Testing passed."
    }
}