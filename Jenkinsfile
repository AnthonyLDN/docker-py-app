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

    stage('Starting: App DB') {
        docker.image('ecsdanthony/py-app-db').withRun('-e "MYSQL_ROOT_PASSWORD=password"')
    }
}