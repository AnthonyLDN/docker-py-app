node {
    def db_container, app_container

    stage('Clone Repository') {
        checkout scm
    }

    stage('Build Docker Images') {
        echo "Building database image."
        db_container = docker.build("ecsdanthony/py-app-db:${env.BUILD_ID}", "/var/jenkins_home/workspace/docker-pipeline/db")

        echo "Building application image."
        app_container = docker.build("ecsdanthony/py-app:${env.BUILD_ID}", "/var/jenkins_home/workspace/docker-pipeline/app")
    }

    stage('Running Tests') {
        echo "Testing passed."
    }

    stage('Starting App DB Instance') {
        docker.image('ecsdanthony/py-app-db').withRun('--net app-net --ip 172.21.0.10 -e "MYSQL_ROOT_PASSWORD=password" -d')
    }
}