pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                // 빌드
                sh 'docker build -t myapp .'
            }
        }
    }
}