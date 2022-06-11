pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Source') {
            steps {
                //git 'https://github.com/srayuso/unir-cicd.git'
                git 'https://github.com/jsgiraldoh/unir-test.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building stage!'
                sh 'make build test-unit'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make build test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
    }
}