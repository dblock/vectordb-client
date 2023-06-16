from typing import Dict
from base64 import b64encode
from vectordb.common.auth.credentials import Credentials

class BasicAuth(Credentials):
    @property
    def username(self) -> str:
        return self._username
    
    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password

    @property
    def _base64_encoded_credentials(self) -> str:
        return b64encode(bytes(f'{self._username}:{self._password}', encoding='ascii')).decode('ascii')

    @property
    def headers(self) -> Dict:
        headers = {}
        headers['Authorization'] = f'Basic {self._base64_encoded_credentials}'
        return headers
