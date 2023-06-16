from vectordb.common.databases.database import Database
from vectordb.databases.open_search.open_search_index import OpenSearchIndex
from vectordb.databases.open_search.open_search_indices import OpenSearchIndices

class OpenSearchDatabase(Database):
    @property
    def indices(self) -> OpenSearchIndices:
        if not self._indices:
            data = self._connection.get(path = '/_cat/indices')
            coll = list(map(lambda idx: OpenSearchIndex(name=idx['index'], data=idx, database=self), data.json()))
            self._indices = OpenSearchIndices(
                database=self, 
                collection=coll
            )
        return self._indices

    def create_index(self, name: str, options={}) -> OpenSearchIndex:
        data = self._connection.put(path = f'/{name}', data={ 
            'settings': {
                'index.knn': True
            },
            'mappings': {
                'properties': {
                    'vector': {
                        'type': 'knn_vector'
                    } | options
                }
            } 
        })
        index = OpenSearchIndex(name=name, database=self)
        if self._indices:
            self._indices[name] = index
        return index
