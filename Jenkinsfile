pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Cloning from GitHub') {
            steps {
                script {
                    echo 'Cloning from GitHub'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/Saravanakumar-SKASC/MLOPS-PROJECT-2.git'
                        ]]
                    )
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    echo 'Creating virtual environment'
                    sh '''
                        python3 -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip setuptools wheel
                        pip install -e .
                        pip install dvc
                    '''
                }
            }
        }

        stage('DVC Pull') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Running DVC pull'
                        sh '''
                            . ${VENV_DIR}/bin/activate
                            dvc pull
                        '''
                    }
                }
            }
        }
    }
}
