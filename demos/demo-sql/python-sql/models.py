from dataclasses import dataclass


# https://docs.python.org/3/library/dataclasses.html
@dataclass()
class Single:
    single_id: int
    titre: str
    duree: int

    def __eq__(self, other):
        return self.single_id == other.single_id and self.titre == other.titre and self.duree == other.duree