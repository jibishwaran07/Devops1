pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo "Hello from Jenkins on Linux!"
            }
        }

        stage('Run Script') {
            steps {
                sh 'echo Running a shell command...'
                sh 'echo Pipeline working successfully!'
            }
        }
    }
}
