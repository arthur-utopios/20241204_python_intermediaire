from dataclasses import dataclass
import datetime


@dataclass
class User:
    id: int
    username: str
    password: str
    created_at: datetime
    last_connection: datetime