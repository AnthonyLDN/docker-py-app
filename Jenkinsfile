pipeline {
    agent any
    def xxx="${env.JENKINS_URL}"
    stages {
        stage('Example') {
            steps {
                echo "Running ${env.BUILD_ID} on ${xxx}"
            }
        }
    }
}