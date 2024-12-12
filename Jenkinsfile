pipeline {
    agent none
    stages {
        stage('nodejs test') {
            agent { label 'nodejs'}
            steps {
                sh 'node --version'
            }
        }
        stage('xcode test') {
            agent { label 'xcode'}
            steps {
                sh 'xcodebuild -version'
            }
        }
    }
}