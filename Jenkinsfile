pipeline {
    agent {
        label 'master'
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
                sh 'make build'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
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