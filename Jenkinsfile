pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
        GCP_PROJECT = "resolute-fold-458114-c1"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
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

        stage('Build and Push Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Build and Push Image to GCR'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}
                            gcloud auth configure-docker --quiet
                            docker build -t gcr.io/${GCP_PROJECT}/mlops-project-2:latest .
                            docker push gcr.io/${GCP_PROJECT}/mlops-project-2:latest
                        '''
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Deploy to Kubernetes'
                        sh '''
                            export PATH=$PATH:${GCLOUD_PATH}:${KUBECTL_AUTH_PLUGIN}
                            gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                            gcloud config set project ${GCP_PROJECT}
                            gcloud container clusters get-credentials mlops-cluster-1 --region us-central1
                            kubectl apply -f deployment.yaml
                        '''
                    }
                }
            }       
        }
    }
}
