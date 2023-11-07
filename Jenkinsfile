pipeline {
    agent any
    stages {

        stage('Build') {
            steps {
                sh "chmod +x -R ${env.WORKSPACE}"
                sh "apt install -y python3-pip"
                sh "apt install -y python3-pymssql"
                sh "apt install -y python3-dotenv"
                sh "apt install -y python3-pytest"
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