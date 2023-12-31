import os
from typing import Any

from vectordb.common.databases.index import Index

class PineconeIndex(Index):
    @property
    def project_id(self) -> str:
        return os.getenv('PROJECT_ID')
    
    def upsert(self, vectors: list, namespace: str = None) -> None:
        data = {
            'vectors' : vectors,
            'namespace' : namespace
        }
        response = self.database._connection.post(namespace=f'{self.name}-{self.project_id}.svc', path='/vectors/upsert', data=data)

    def delete(self) -> None:
        self.database._connection.delete(path=f'/databases/{self.name}')

    def query(self, vector: list, top_k: int, namespace: str = None) -> Any:
        data = {
            'vector' : vector,
            'top_k' : top_k,
            'namespace' : namespace
        }
        response = self.database._connection.post(namespace=f'{self.name}-{self.project_id}.svc', path='/query', data=data)
        return response.json()
