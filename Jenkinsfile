node {
    def db_container, app_container

    stage('Clone Repository') {
        checkout scm
    }

    stage('Build Docker Images') {
        echo "Building database image."
        db_container = docker.build("ecsdanthony/py-app-db", "/var/jenkins_home/workspace/docker-pipeline/db")

        echo "Building application image."
        app_container = docker.build("ecsdanthony/py-app", "/var/jenkins_home/workspace/docker-pipeline/app")
    }

    stage('Running Tests') {
        echo "Testing passed."
    }

    stage('Start: App DB') {
        sh "docker run --net app-net --ip 172.21.0.10 -e MYSQL_ROOT_PASSWORD=password -d ecsdanthony/py-app-db"
    }
}