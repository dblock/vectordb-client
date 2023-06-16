from vectordb.common.databases.database import Database
from vectordb.common.databases.index import Index
from vectordb.common.databases.indices import Indices
from vectordb.databases.pinecone.pinecone_indices import PineconeIndices
from vectordb.databases.pinecone.pinecone_index import PineconeIndex

class PineconeDatabase(Database):
    @property
    def indices(self) -> Indices:
        if not self._indices:
            data = self._connection.get('/databases')
            data.raise_for_status() # todo: generalize error
            coll = list(map(lambda idx: PineconeIndex(idx), data.json()))
            self._indices = PineconeIndices(
                database=self, 
                collection=coll
            )
        return self._indices

    def create_index(self, name: str, options={}) -> Index:
        data = self._connection.post('/databases', data={ 'name': name } | options)
        data.raise_for_status() # todo: generalize error
        return PineconeIndex(name)

    def delete_index(self, name: str, options={}) -> Index:
        data = self._connection.delete(f'/databases/{name}', options)
        data.raise_for_status() # todo: generalize error

