from vectordb.common.databases.database import Database
from vectordb.common.databases.index import Index
from vectordb.common.databases.indices import Indices
from vectordb.databases.pinecone.pinecone_indices import PineconeIndices
from vectordb.databases.pinecone.pinecone_index import PineconeIndex

class PineconeDatabase(Database):
    @property
    def indices(self) -> Indices:
        if not self._indices:
            data = self._connection.get(namespace ='controller', path = '/databases')
            data.raise_for_status() # todo: generalize error
            coll = list(map(lambda idx: PineconeIndex(name=idx, database=self), data.json()))
            self._indices = PineconeIndices(
                database=self, 
                collection=coll
            )
        return self._indices

    def create_index(self, name: str, options={}) -> Index:
        data = self._connection.post(namespace ='controller', path = '/databases', data={ 'name': name } | options)
        data.raise_for_status() # todo: generalize error
        index = PineconeIndex(name=name, database=self)
        if self._indices:
            self._indices[name] = index
        return index
