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
        stage('e2e tests') {
            steps {
                sh 'make build test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always{
            junit 'results/*_result.xml'
            //cleanWs()
            
            archiveArtifacts artifacts: 'results/*.xml', onlyIfSuccessful: true
            emailext to: "johansebastiangh@gmail.com",
            subject: "jenkins build:${currentBuild.currentResult}: ${env.JOB_NAME}",
            body: "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nMore Info can be found here: ${env.BUILD_URL}",
            attachmentsPattern: 'results/*.xml'    
            cleanWs()
        }
    }

}