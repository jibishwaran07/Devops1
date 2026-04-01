stage('SonarQube Analysis') {
    steps {
        sh """
            docker run --rm \
              --network sonar-net \
              -e SONAR_HOST_URL=http://sonarqube:9000 \
              -e SONAR_LOGIN=sqp_4160bcd9f13efe13aae51dbc5cd27a32aea1aa9 \
              -v "\$(pwd):/usr/src" \
              sonarsource/sonar-scanner-cli:5
        """
    }
}
