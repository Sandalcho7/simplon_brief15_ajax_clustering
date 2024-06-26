# SIMPLON DEV IA | Brief 15

## Clustering

### Contexte

Ce projet a été réalisé dans le cadre de la formation de développement en intelligence artificielle chez Simplon.<br>

Il s'agit de découvrir les différents modèles de clustering et de les exposer sur un frontend, l'occasion aussi de mettre en place un déploiement continu sur Azure, via GitHub Actions.

### Data

[Lien vers les données à utiliser](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

### Structure du projet

```bash
project/
│
├── .github/
│   └── workflows/
│       └── dev-deployment.yml    # Worflow de déploiement sur l'environnement de dev
│       └── main-deployment.yml    # Worflow de déploiement sur l'environnement de prod
│
├── backend/
│   ├── data/
│   │   └── mall_customers.csv    # Emplacement des données
│   ├── pkl/    # Dossier généré après génération des .pkl (pkl_gen.py)
│   │   ├── dbscan.pkl
│   │   └── kmeans.pkl
│   ├── .dockerignore
│   ├── config.py    # Config pour le backend (emplacement des données, etc.)
│   ├── Dockerfile
│   ├── main.py    # API
│   ├── pkl_gen.py    # Script à exécuter pour générer les modèles .pkl
│   ├── plotting.py    # Fonctions de génération des plots pour chaque modèle
│   ├── processing.py    # Fonction de processing des données
│   ├── scoring.py    # Fonctions de scoring (silhouette score) pour chaque modèle
│   ├── requirements.txt
│   ├── spec.md    # Spécifications de l'API
│   └── testing.py    # Fonctions de test avant déploiement
│
├── frontend/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── config_deploy_dev.yml    # Configuration de l'instance de conteneur pour le déploiement en dev
├── config_deploy_main.yml    # Configuration de l'instance de conteneurs pour le déploiement en prod
└── README.md
```
### Notes

Ce projet a été développé pour être déployé sur Azure via Github Actions, il est cependant possible de le faire tourner en local avec la procédure ci-dessous.

### Procédure en local

1 / Avant de démarrer le projet, il est nécessaire d'installer certaines dépendances sur l'environnement de travail. Pour effectuer ces installations, vous pouvez éxécuter la commande suivante :
```bash
pip install -r backend/requirements.txt
```
2 / Depuis le terminal, placez-vous dans le dossier backend/, générez les modèles .pkl en exécutant le script :
```bash
python pkl_gen.py
```
3 / Depuis le terminal, lancer l'API en se plaçant dans le dossier backend/ et en exécutant :
```bash
python main.py
```
Penser à changer l'API_PATH dans le script.js, en local il devrait s'agir de :
```js
const API_PATH = "http://localhost:8000"
```
4 / Depuis le terminal, se placer dans le dossier frontend/ et exécuter cette ligne de commande :
```bash
python -m http.server 8001
```
5 / Se rendre à l'adresse http://localhost:8001 pour consulter la page et communiquer avec l'API.

### Améliorations possibles
J'aurais aimé intégrer, dans mes fichiers config_deploy.yml, les variables d'environnements définies dans mes workflows GitHub Actions. Actuellement, il faut modifier les fichiers config dès que les variables changent dans les workflows. Ce n'est pas complètement dynamique.