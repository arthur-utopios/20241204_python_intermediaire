class Personne:
    def __init__(self, nom: str, age: int, secret: str) -> None:
        self.nom = nom  # public
        self.prenom = "michel"
        self._age = age  # protégé
        self.__secret = secret  # privé

    def get_secret(self) -> str:
        return len(self.__secret) * "*"

    def set_secret(self, value) -> None:
        self.__secret = value

    # Permet d'accéder à l'attribut privé __secret comme si c'était une variable!
    @property
    def secret(self):
        return len(self.__secret) * "*"

    # Setter: permet de mettre à jour la propriété
    @secret.setter
    def secret(self, value):
        if len(value) < 5:
            raise ValueError("Le secret est trop court")
        self.__secret = value

    @secret.deleter
    def secret(self):
        self.__secret = ""

    @property
    def full_name(self) -> str:
        return f"{self.prenom} {self.nom.upper()}"
    
    def get_full_name(self) -> str:
        return f"{self.prenom} {self.nom.upper()}"



if __name__ == "__main__":
    ma_personne = Personne("Jean", 45, "Z$wOc;_13°")
    # print(ma_personne.__secret) # Lève une exception

    # Les propriétés privées en Python ne le sont pas vraiment
    # C'est comme mettre la clé sous le tapis
    print(ma_personne._Personne__secret)

    print(ma_personne._age)  # On peut également accéder aux membres protégés

    # Sans les propriétés
    print(ma_personne.get_secret())
    ma_personne.set_secret("bonjour")
    print(ma_personne.get_secret())

    # Avec les propriétés
    print(ma_personne.secret)

    ma_personne.secret = "toto23bis"

    # Exemple de propriété calculée : créé à partir d'autres éléments de la classe
    print(ma_personne.full_name)
    ma_personne.full_name = "Michel ROBERT"
    print(ma_personne.get_full_name())
