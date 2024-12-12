from basedao import BaseDAO
from models import Single


class SingleDAO(BaseDAO):
    def get_one_by_id(self, id: int):
        query = "SELECT single_id, titre, duree FROM single WHERE single_id = ?"
        with self._con.cursor() as cur:
            cur.execute(query, (id,))
            # Déplace le curseur sur le premier enregistrement
            single = cur.fetchone()  # renvoie un single ou None
            return single

    def get_all(self):
        query = "SELECT single_id, titre, duree FROM single"
        with self._con.cursor() as cur:
            cur.execute(query)
            singles = []
            for (single_id, titre, duree) in cur:
                singles.append(Single(single_id, titre, duree))
            return singles


    def save(self, obj):
        if obj.single_id:
            self._update(obj)
        else:
            self._create(obj)

    def delete(self, id):
        raise NotImplementedError

    def _update(self, obj):
        query = "UPDATE single SET titre = ?, duree = ? WHERE single_id = ?"
        parameters = (obj.titre, obj.duree, obj.single_id)
        with self._con.cursor() as cur:
            cur.execute(query, parameters)
            self._con.commit()

    def _create(self, obj):
        query = "INSERT INTO single (titre, duree) VALUES (?, ?)"
        parameters = (obj.titre, obj.duree)
        with self._con.cursor() as cur:
            cur.execute(query, parameters)
            self._con.commit()
