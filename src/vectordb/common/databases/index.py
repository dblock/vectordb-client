from abc import ABC, abstractmethod
from typing import Any

class Index(ABC):
    @property
    def name(self) -> str:
        return self._name

    @property
    def database(self) -> Any:
        return self._database

    def __init__(self, database: Any, name: str, data=None) -> None:
        self._name = name
        self._database = database
        self._data = data

    @abstractmethod
    def delete(self, options = None) -> None:
        pass

    @abstractmethod
    def upsert(self, vectors: list, namespace: str = None) -> None:
        pass

    @abstractmethod
    def query(self, vector: list, top_k: int, namespace: str = None) -> Any:
        pass
