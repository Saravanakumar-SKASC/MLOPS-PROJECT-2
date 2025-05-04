pipeline{
    agent any

    stages{
        stage('cloning from github'){
            steps{
                script{
                    echo 'Cloning from github'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Saravanakumar-SKASC/MLOPS-PROJECT-2.git']])
                }

            }
        }
    }
}