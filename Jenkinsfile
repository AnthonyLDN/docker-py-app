pipeline {
    def db, app

    stages {
        stage('Clone Repository') {
            checkout scm
        }

        stage('Build Docker Images') {
            steps {
                sh 'echo "Building database image."'
                db = docker.build(
                    "py-app-db",
                    "/var/jenkins_home/workspace/docker-pipeline/db"
                )
            }
        }
    }
}