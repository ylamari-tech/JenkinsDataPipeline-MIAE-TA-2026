pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('1. Setup Environment') {
            steps {
                echo 'Préparation de l'environnement Python...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('2. Extract (Ingestion)') {
            steps {
                echo 'Étape 1 : Extraction des données source...'
                sh './venv/bin/python scripts/extract.py'
            }
        }

        stage('3. Transform (Data Prep)') {
            steps {
                echo 'Étape 2 : Nettoyage et transformation...'
                sh './venv/bin/python scripts/transform.py'
            }
        }

        stage('4. Load & Quality Check') {
            steps {
                echo 'Étape 3 : Chargement SQLite et vérification...'
                sh './venv/bin/python scripts/load.py'
            }
        }
    }

    post {
        always {
            echo 'Archivage des artéfacts du pipeline...'
            archiveArtifacts artifacts: '*.csv, *.json, *.db', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline Data exécuté avec succès !'
        }
        failure {
            echo 'Échec du pipeline Data.'
        }
    }
}
