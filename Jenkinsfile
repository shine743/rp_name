pipeline {
    agent any
    stages {
        stage('nodejs test') {
            steps {
                sh 'node --version'
            }
        }
        stage('xcode test') {
            steps {
                sh 'xcodebuild -version'
            }
        }
    }
}