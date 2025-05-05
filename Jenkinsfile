pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Sh-bit01/Jenkins_git.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh './venv/bin/python app.py &'
                sh 'sleep 5'  // give app time to start
                sh 'curl http://localhost:5000'
            }
        }
    }
}
