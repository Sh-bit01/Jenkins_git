pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Sh-bit01/Jenkins_git.git'
            }
        }

   stage('Build Docker Image') {
    steps {
        sh 'docker build -t my-python-app .'
    }
}

stage('Run App in Docker') {
    steps {
       sh  'docker rm -f my-python-app-container || true'
	sh 'docker run -d --name my-python-app-container -p 5000:5000 my-python-app'

        sh 'sleep 5'
        sh 'curl http://localhost:5000'
    }
}

    }
}
