from abc import ABC, abstractmethod

from mariadb import Connection, connect


class BaseDAO(ABC):

    _con: Connection

    def __init__(self):
        super().__init__()
        self._con = connect(user="root", password="", host="127.0.0.1", database="demo_rock")

    @abstractmethod
    def get_one_by_id(self, id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
