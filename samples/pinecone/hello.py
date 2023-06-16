#!/usr/bin/env python

import os

from vectordb.databases.pinecone.pinecone_database import PineconeDatabase
from vectordb.common.auth.api_token import ApiToken
from vectordb.common.transport.http_transport import HttpTransport

def main():
    with HttpTransport(endpoint=os.getenv('ENDPOINT')) as http:
        db = PineconeDatabase(connection = http)
        auth = ApiToken(token=os.getenv('API_TOKEN'))
        db.connect(auth)

        if not 'my-index' in db.indices:
            index = db.create_index('my-index', { 'dimension': 3 })
            print(f'\nIndex: {index}')
    
        print(f'\nIndices: {len(db.indices)}')
        for idx in db.indices:
            print(f'idx={idx}')

        db.indices['my-index'].upsert(
            vectors=[
                {
                    'id': 'vec1',
                    'values': [0.1, 0.2, 0.3],
                    'metadata': {'genre': 'drama'},
                    'sparse_values': {
                        'indices': [10, 45, 16],
                        'values': [0.5, 0.5, 0.2]
                    }
                },
                {
                    'id': 'vec2',
                    'values': [0.2, 0.3, 0.4],
                    'metadata': {'genre': 'action'},
                    'sparse_values': {
                        'indices': [15, 40, 11],
                        'values': [0.4, 0.5, 0.2]
                    }
                }
            ],
            namespace='example-namespace'
        )

        results = db.indices['my-index'].query(
            vector=[0.1, 0.2, 0.3],
            top_k=1,
            namespace='example-namespace'
        )
        
        print(results)

        # db.indices['my-index'].delete()

if __name__ == "__main__":
    main()
