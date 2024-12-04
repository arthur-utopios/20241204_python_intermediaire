# Création d'une classe statique
class UtilitaireMath:

    # Une méthode statique n'utilise aucun élément de classe
    @staticmethod
    def addition(a: float | int, b: float | int) -> float | int:
        return a + b
    

class CompteBancaire:
    taux_interet = 0.05 # attribut de classe

    def __init__(self, solde: float) -> None:
        self.solde = solde

    # une méthode de classe nécessite d'utiliser un élément de la classe
    @classmethod
    def set_taux_interet(cls, value: float) -> None:
        cls.taux_interet = value

    @classmethod
    def init_objet_defaut(cls):
        return cls(0)

    def calculer_interet(self):
        return self.solde * self.taux_interet


if __name__ == "__main__":
    print(UtilitaireMath.addition(12, 50))
    print(UtilitaireMath().addition(12, 50))

    compte01 = CompteBancaire(100)
    compte02 = CompteBancaire(200)
    compte03 = CompteBancaire(300)

    print(compte01, compte01.calculer_interet())
    print(compte02, compte02.calculer_interet())
    print(compte03, compte03.calculer_interet())

    CompteBancaire.set_taux_interet(0.10)
    CompteBancaire.taux_interet = 0.10

    print(compte01, compte01.calculer_interet())
    print(compte02, compte02.calculer_interet())
    print(compte03, compte03.calculer_interet())

    compte_defaut = CompteBancaire.init_objet_defaut()
    print(compte_defaut)

