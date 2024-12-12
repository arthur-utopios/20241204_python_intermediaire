# Formation Python Intermédiaire

## Ressources

## Créer un snippet

1. Ouvrir la palette de commandes : `CTRL + SHIFT + P`
2. Taper : `Snippet` et sélectionner `Configure snippets`
3. Sélectionner le snippet pour le langage souhaité
4. Dans le code ajouter le snippet souhaité:

```json
"if(main)": {
    "prefix": "if(main)",
    "body": ["if __name__ == \"__main__\":", "    ${1:pass}"],
    "description": "Code snippet for a `if __name__ == \"__main__\": ...` block"
},
```

## Formater son code

Par convention, il est intéressant de formater son code à l'aide de la [PEP8](https://peps.python.org/pep-0008/).
Pour cela on peut utiliser des formateurs existants pour python, notamment:

1. [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
2. [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) : plus performant et plus récent

## Ressources SQL

- [sql.sh](https://sql.sh/)
- [documentation mariadb](https://mariadb.com/kb/en/sql-statements-structure/)

## Création d'un environnement

1. Créer l'environnement avec la commande suivante:

```sh
python -m venv ./.venv
```

2. Activer l'environnement virtuel

```sh
# Windows
tutorial-env\Scripts\activate

# Linux / MacOS
source tutorial-env/bin/activate
```

3. Quitter l'environnement virtuel

```sh
deactivate
```

4. Geler les dépendances

```sh
pip freeze > requirements.txt
```

5. Installer le projet avec ses dépendances

```sh
pip install -r ./requirements.txt
```

## Gestionnaires de packages
