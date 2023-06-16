from typing import Dict
from vectordb.common.auth.credentials import Credentials

class ApiToken(Credentials):
    @property
    def token(self) -> str:
        return self._token
    
    def __init__(self, token) -> None:
        self._token = token

    @property
    def headers(self) -> Dict:
        headers = {}
        headers['Api-Key'] = self._token
        return headers
