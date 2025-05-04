pipeline{
    agent any
    environment{
        VENV_DIR = "venv"
    }

    stages{
        stage('cloning from github'){
            steps{
                script{
                    echo 'Cloning from github'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/Saravanakumar-SKASC/MLOPS-PROJECT-2.git']])
                }

            }
        }
        stage('making a virtual environment'){
            steps{
                script{
                    echo 'making a virtual environment'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc
                    '''

            }
        }
    }
    stage('DVC pull'){
            steps{
                  withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                script{
                        echo 'DVC pull'
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