pipeline {
    agent any
    stages {

        stage('Build') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "apt install -y python3-pip"
                sh "pip install -r requirements.txt"
            }
        }
        stage('Test') {
            steps {
                echo 'Starting tests....'
                sh "./demo_run.sh"
            }
        }
    }
}