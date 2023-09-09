# Projet 4: Chess Tournament

Ce programme est un gestionnaire de tournois afin d'être utilisé par le club d'échec local.
Il fonctionne hors ligne, permet de sauvegarder et de revoir les résultats des tournois.

## Comment installer le programme ? 
- Installer Python
- Télécharger le programme

`git clone https://github.com/ClaireRuysschaert/OC_P4_MVC_Chess_Tournament.git`
- Placez vous dans le dossier "OC_P4_MVC_Chess_Tournament"
- Créer un nouvel environnement virtuel et activez le `python -m venv .venv`

Linux:
`source .venv/bin/activate`

Windows:
`env\scripts\activate.bat`
- Installer les packages requis pour faire fonctionner le programme

`pip install -r requirements.txt`

## Comment lancer le programme ?
Lancez la commande ci-dessous:
(Pensez à vérifier que vous avez bien activé votre environnement virtuel.)

`python run.py`

## Utilisation
Le menu principal est divisé en 4 fonctionnalités.

1. Créer un tournoi
- Cette section vous permet de créer un tournoi et d'y indiquer toutes les informations le concernant (nom, lieu, nombre de joueurs, description pour les remarques générales du directeur du tournoi, nombre de tours).
- Le tournoi sera alors créé et enregistré dans la base de données. Il possèdera un ID qui vous sera indiqué à l'écran. Veuillez vous le noter pour charger et jouer ce tournoi ou pour afficher les rapports.
- Vous aurez alors le choix de sélectionner un joueur existant dans la base de données ou alors d'en créer de nouveaux. Vous avez la possibilité de n'entrer qu'une partie des participants. L'autre partie pourra être ajoutée dans la section 2, avant de jouer le tournoi, ou alors directement dans la section 3, de création des joueurs.

2. Charger et jouer un tournoi
- Cette section vous permet de charger un tournoi depuis la base de données. Lors du chargement, le programme va vérifier que tous les joueurs ont été inscrits au tournoi. S'il manque des joueurs vous serez convié à renseigner tous les joueurs participant au tournoi. Si tout est en ordre, la liste des joueurs du tournoi sera affichée. 
- Le programme créé de manière aléatoire pour le premier tour, puis de manière logique les paires de joueurs s'affrontant. Vous aurez pour chaque tour un listing des INE des joueurs ainsi que l'ID du match. Ce dernier vous sera demandé pour jouer les matchs. Vous pouvez les jouer à n'importe quel moment. Si vous quittez le programme, les informations renseignées seront enregistrées dans la base de données et vous pourrez renseigner les gagnants à tout moments. 
- Enfin, à la fin de chaque tour et à la fin du tournoi, il vous sera affiché un classement des joueurs ainsi que leur score.

3. Créer des joueurs
- Cette section vous permet de créer des joueurs et d'y indiquer toutes les informations les concernant (identifiant national d'échecs, prénom, nom et date de naissance)
- Le programme vérifie si l'ine du joueur indiqué existe déjà dans la base de données.

4. Afficher les rapports
Cette section vous permet de générer 5 différents rapports : 
- liste de tous les joueurs par ordre alphabétique
- liste de tous les tournois 
- nom et dates d’un tournoi donné
- liste des joueurs du tournoi par ordre alphabétique
- liste de tous les tours du tournoi et de tous les matchs du tour.

## Comment générer un nouveau rapport flake8 ? 
Flake8 est un plugin en Python permettant de générer des rapports HTML détaillant les violations des normes de codage détectées par l'outil Flake8. Ces rapports offrent une vue d'ensemble des problèmes de conformité du code source.

Lancez la commande suivante `flake8 --format=html --htmldir=flake-report`. 
Celle-ci va créer un dossier "flake-report" qui contiendra le rapport flake8 généré au format html.