import os
import unittest
from vectordb.databases.pinecone.pinecone_database import PineconeDatabase
from vectordb.common.auth.api_token import ApiToken
from vectordb.common.transport.http_transport import HttpTransport

class PineconeDatabaseTest(unittest.TestCase):
    def test_example(self) -> None:
        with HttpTransport(endpoint=os.getenv('ENDPOINT')) as http:
            db = PineconeDatabase(connection = http)
            auth = ApiToken(token=os.getenv('API_TOKEN'))
            db.connect(auth)

            if not 'my-index' in db.indices:
                index = db.create_index('my-index', { 'dimension': 1024 })
                print(f'\nIndex: {index}')
        
            print(f'\nIndices: {len(db.indices)}')
            for idx in db.indices:
                print(f'idx={idx}')
        
            db.delete_index('my-index')