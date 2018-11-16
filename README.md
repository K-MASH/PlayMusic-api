# Play_Zik

## General
- kMash_001
- CdP: Duhamel Stuf, Andresse Njeungoue
- dev: Andresse Njeungoue
- Dossier Drive: https://drive.google.com/drive/u/0/folders/1g_UIhsdcDAWL6iNIS7r5eAfxd9Pu_QO9

## GCP
- project: https://console.cloud.google.com/home/dashboard?project=play-zik
- scope: Social

# Qu'est ce que c'est (technos)

Application web AppEngine / Python 2.7 / Flask / Android / APIs Google (Admin SDK)[Cloud storage]

# Qu'est ce que ça fait

cf specs dans le dossier Drive.

# Installation

```bash
./tasks/setup.sh <path to Gcloud appengine sdk>
```

# Execution

```bash
source venv/bin/activate
dev_appserver.py api.yaml dispatch.yaml
# ... then
deactivate
```

# Deploiement

```bash
./tasks/deploy.sh <dev|production|acceptance> <version>
```

