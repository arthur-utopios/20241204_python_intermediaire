class Animal:
    # On redéfinit le constructeur de object
    def __init__(self, nom: str) -> None:
        if not nom:
            raise ValueError("Nom obligatoire")
        self.nom = nom

    def parler(self) -> str:
        raise NotImplementedError("Non implémentée")


class Chien(Animal):
    def __init__(self, nom: str, race: str) -> None:
        super().__init__(nom) # Grâce à la fonction super() on peut accéder aux éléments du parent
        self.race = race


    def parler(self) -> str:
        return "woof"

class Chat(Animal):
    def __init__(self, nom: str, couleur: str) -> None:
        super().__init__(nom)
        self.couleur = couleur

    def parler(self) -> str:
        return "meow"

if __name__ == "__main__":
    mon_objet = object()  # Toute classe hérite de object

    rex = Chien("Rex", "Berger allemand")
    print(rex.parler())

    garfield = Chat("Garfield", "Roux")
    print(garfield.parler())