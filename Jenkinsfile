pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Frapas1/Temperature_Converter.git']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'master', url: 'https://github.com/Frapas1/Temperature_Converter.git'
                sh 'python3 --version'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}