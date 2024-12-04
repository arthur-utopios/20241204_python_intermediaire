class CompteBancaire:

    # Constante qui est partagée entre toutes les instances de la classe CompteBancaire
    TAUX_AGIOS = 0.05

    def __init__(self, numero_compte: str, nom: str, solde: float) -> None:
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__solde = solde

    def versement(self, montant: float) -> None:
        self.__solde += abs(montant)

    def retrait(self, montant: float) -> None:
        self.__solde -= abs(montant)

    def agios(self, taux_agios: float) -> None:
        if self.__solde < 0:
            self.__solde *= 1 + taux_agios

    def afficher(self) -> None:
        print(f"COMPTE N° {self.__numero_compte}\n> Nom: {self.__nom}\n> Solde: {self.__solde:0.2f}€")

if __name__ == "__main__":
    compte = CompteBancaire("293409592", "Livre épargne", 100)
    compte.afficher()

    compte.versement(100)
    compte.afficher()

    compte.retrait(250)
    compte.agios(0.05)
    compte.afficher()
    compte.agios(CompteBancaire.TAUX_AGIOS)
    compte.afficher()
    compte.TAUX_AGIOS