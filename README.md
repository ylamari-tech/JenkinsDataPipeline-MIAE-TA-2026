# Jenkins Data Pipeline (ETL Débutant)

Ce projet est un exemple simple de pipeline ETL (Extract, Transform, Load) automatisé avec **Jenkins** et **Python**.

## 📁 Structure du projet

```text
jenkins-data-pipeline/
├── scripts/
│   ├── extract.py      # Récupère les données météo depuis l'API Open-Meteo (raw_data.json)
│   ├── transform.py    # Filtre et nettoie les données (cleaned_data.csv)
│   └── load.py         # Charge les données dans SQLite (weather.db) et valide la qualité
├── Jenkinsfile         # Définition du pipeline CI/CD Jenkins
├── requirements.txt    # Dépendances Python nécessaires
└── README.md           # Documentation du projet
```

## 🚀 Prérequis

* **Python 3.8+**
* **Jenkins** installé et fonctionnel
* **Git**

## 🛠️ Exécution locale sans Jenkins

Si vous désirez tester les scripts manuellement :

```bash
# 1. Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Sur Linux/macOS
# venv\Scripts\activate   # Sur Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Exécuter l'ETL étape par étape
python scripts/extract.py
python scripts/transform.py
python scripts/load.py
```

## ⚙️ Configuration dans Jenkins

1. **Initialiser un dépôt Git** dans le dossier du projet :
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Data pipeline ETL"
   ```
2. **Créer un Job dans Jenkins** :
   * Nom du job : `data-pipeline-meteo`
   * Type : **Pipeline**
3. **Configurer la source du Pipeline** :
   * Dans la section *Pipeline*, choisissez **Pipeline script from SCM**.
   * SCM : **Git** (fournissez le chemin vers votre dépôt distant ou local).
   * Script Path : `Jenkinsfile`.
4. **Lancer la construction** :
   * Cliquez sur **Build Now** (Lancer le build).
