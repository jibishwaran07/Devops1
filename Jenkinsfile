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
                sh 'python3 python4.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=Devops1 \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://localhost:9000 \
                      -Dsonar.login=sqp_4160bcd9f13efe13aae51dbc5cd27a32aea1aa9
                '''
            }
        }
    }
}
