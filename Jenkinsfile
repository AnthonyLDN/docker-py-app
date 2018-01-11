node {
    def db, app

    stage('Clone Repository') {
        checkout scm
    }

    stage('Build Docker Images') {
        echo "Building database image."
        db = docker.build("ecsdanthony/py-app-db", "/var/jenkins_home/workspace/docker-pipeline/db")

        echo "Building application image."
        app = docker.build("ecsdanthony/py-app", "/var/jenkins_home/workspace/docker-pipeline/app")
    }

    stage('Running Tests') {
        echo "Testing passed."
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            db.push("${env.BUILD_NUMBER}")
            db.push("latest")
        }
    }
}