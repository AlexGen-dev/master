pipline {
    agent any
    stages {
        stage ('Project 1') {
            steps {
                echo 'Hello world'
            }
        }
    }
}