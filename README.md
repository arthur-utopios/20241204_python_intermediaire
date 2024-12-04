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
