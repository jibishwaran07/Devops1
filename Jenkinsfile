pipeline {
    agent any

    stages {
        stage('Run Shell Script') {
            steps {
                sh './script.sh'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}
