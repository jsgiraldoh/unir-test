pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/jsgiraldoh/unir-test.git'
            }
        }
        stage('Unit tests') {
            steps {
                echo 'Unit tests!'
                sh 'make build test-unit'
            }
        }
        stage('Api tests') {
            steps {
                echo 'Api tests!'
                sh 'make build test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2e tests') {
            steps {
                echo 'E2e tests!'
                sh 'make build test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('Email Notification') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    echo 'Email Notification!'
                    emailext body: 'Test Message',
                        subject: 'Test Subject',
                        to: 'test@example.com'
                }    
            }
        }
    }
    post {
        always{
            junit 'results/*_result.xml'
            cleanWs()
        }
    }

}