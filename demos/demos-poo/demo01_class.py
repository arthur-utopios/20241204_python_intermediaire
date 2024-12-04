from demo02_visibility_property import Chien
import os

class Personne:
    # Cette méthode est le constructeur de la classe
    # Elle permet de définir quels sont les attributs nécessaire à la construction de mon objet
    def __init__(self, prenom: str, nom: str, age: int) -> None:
        # Self représente l'instance de l'objet qui est créé
        # Python va automatiquement le passer en paramètre lors de la création de l'objet
        self.prenom = prenom  # Attribut d'une instance
        self.nom = nom
        self.age = age

    # Méthode d'instance (on lui passe le paramètre self!)
    def se_presenter(self) -> None:
        """Affiche les informations d'une personne"""  # Permet de documenter les méthodes
        print(f"Bonjour je m'appelle {self.prenom} et j'ai {self.age} ans.")


# On stocke le code exécutant dans cette condition !
if __name__ == "__main__":
    # Création d'un instance de la classe Personne
    pierre = Personne("Pierre", "Dupont", 24)  # ALT + SHIFT + FLECHE BAS : dupliquer
    marie = Personne("Marie", "Pierre", 32)

    # Utilisation d'un méthode sur un objet
    pierre.se_presenter()
    marie.se_presenter()

    medor = Chien("Médor")
