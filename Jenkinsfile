pipeline {
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Frapas1/Temperature_Converter.git']]])
            }
        }
        stage('Build') {
            agent{
                docker {image 'python3:3.12.0b3-alpine'}
            }
            steps {
                git branch: 'master', url: 'https://github.com/Frapas1/Temperature_Converter.git'
                sh 'python3 ops.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }
    }
}