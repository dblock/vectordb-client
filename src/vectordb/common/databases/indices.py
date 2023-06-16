from typing import Dict, Generic, TypeVar
from abc import abstractmethod
from vectordb.common.databases.index import Index

T = TypeVar('T', bound='Index')
D = TypeVar('D', bound='Database')

class Indices(Dict, Generic[T]):
    @property
    def database(self) -> D:
        return self._database
    
    def __init__(self, database: D, collection = []) -> None:
        self._database = database
        super().__init__({ x.name: x for x in collection })

    def create(self, name: str, options={}) -> Index:
        index = self._database.create_index(name, options)
        self.add(index)
        return index
