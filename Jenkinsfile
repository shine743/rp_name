pipeline {
    agent none
    stages {
        stage('git test') {
            agent any
            steps {
                sh 'git --version'
            }
        }
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
