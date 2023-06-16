import json
import os
from typing import Any

from vectordb.common.databases.index import Index

class OpenSearchIndex(Index):
    def upsert(self, vectors: list, namespace: str = None) -> None:
        data = ""
        for vector in vectors:
            data += json.dumps({
                'index': { '_index' : self.name, '_id' : vector['id'] },
                'vector': vector['values']
            } | { i: vector[i] for i in vector if i != 'id' and i != 'values' }) + "\n"
        response = self.database._connection.post(path='_bulk', data=data)

    def delete(self) -> None:
        data = self.database._connection.delete(path=f'/{self.name}')

    def query(self, vector: list, top_k: int, namespace: str = None) -> Any:
        data = {
            'query': {
                'knn': {
                    'vector': {
                        'vector': vector,
                        'k': top_k 
                    }
                }
            }
        }
        response = self.database._connection.post(path=f'{self.name}/_search', data=data)
        return response.json()
