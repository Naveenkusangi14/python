pipeline {
    agent {
        docker { 
            image 'node:16-alpine' 
            args '-u root:root' // Run as root to avoid permission issues
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}
