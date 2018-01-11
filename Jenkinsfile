pipeline {
    agent any
    def HOME="${env.JENKINS_HOME}"
    stages {
        stage('Example') {
            steps {
                echo "Running ${env.BUILD_ID} on ${HOME}"
            }
        }
    }
}