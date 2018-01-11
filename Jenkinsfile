node {
    def db, app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build images') {
        sh 'echo "Building database image."'
        db = docker.build("db/")
    }
}