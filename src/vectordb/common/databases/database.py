from abc import ABC, abstractmethod

from vectordb.common.auth.credentials import Credentials
from vectordb.common.databases.indices import Indices
from vectordb.common.databases.index import Index
from vectordb.common.transport.transport import Transport

class Database(ABC):
    @property
    def connection(self):
        return self._connection
    
    def __init__(self, connection: Transport) -> None:
        self._connection = connection
        self._indices = None

    def connect(self, credentials: Credentials) -> None:
        self._credentials = credentials
        self._connection.connect(credentials)

    @abstractmethod
    def indices(self) -> Indices:
        pass

    @abstractmethod
    def create_index(self, name: str, options={}) -> Index:
        pass
