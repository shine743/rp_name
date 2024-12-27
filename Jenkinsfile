pipeline {
    agent none
    stages {
        stage('xcode test') {
            agent { label 'xcode'}
            steps {
                sh 'xcodebuild -version'
            }
        }
        stage('nodejs test') {
            agent { label 'nodejs'}
            steps {
                sh 'node --version'
            }
        }
    }
}
