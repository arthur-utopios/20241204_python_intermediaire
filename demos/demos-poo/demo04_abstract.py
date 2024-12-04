from abc import ABC, abstractmethod


# Hériter de ABC permet à une classe d'être abstraite
# Abstraite signifie qu'on ne peut pas instancier la classe
class Animal(ABC):
    def __init__(self, nom: str) -> None:
        self.nom = nom

    # Grâce au décorateur @abstractmethod on peut forcer les enfants à redéfinir une méthode
    @abstractmethod
    def parler(self) -> str:
        pass

    def se_presenter(self) -> str:
        return f"Je suis un {self.__class__.__name__} et je m'apelle {self.nom}"


class Chien(Animal):
    def parler(self) -> str:
        return "woof!"


if __name__ == "__main__":
    # animal = Animal("Animal")
    lassie = Chien("Lassie")
    print(lassie.parler())
