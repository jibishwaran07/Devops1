pipeline {
    agent any

    stages {
        stage('Run Shell Script') {
            steps {
                sh './shellfile.sh'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 python2.py'
            }
        }
    }
}
