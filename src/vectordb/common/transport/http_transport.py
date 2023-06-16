from typing import Any, Dict
from httpx import Client, HTTPTransport
from vectordb.common.transport.transport import Transport
from vectordb.common.auth.credentials import Credentials
from urllib.parse import urljoin

class HttpTransport(Transport):
    def __enter__(self) -> 'HttpTransport':
        return self
    
    def __exit__(self, exc_type: Any, exc_value: Any, exc_traceback: Any) -> None:
        if self._client:
            self._client.__exit__(exc_type, exc_value, exc_traceback)
            self._client = None

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @property
    def user_agent(self) -> str:
        return self._user_agent

    def __init__(self, endpoint, user_agent='VectorDB Client/1.0') -> None:
        # todo: replace hard-coded VectorDB Client/1.0 with dynamic library version
        self._endpoint = endpoint
        self._user_agent = user_agent

    def connect(self, credentials: Credentials) -> None:
        self._client = Client()
        self._credentials = credentials
        self._headers = None

    @property
    def headers(self) -> Dict:
        if not self._headers:
            headers = self._credentials.headers.copy()
            headers['User-agent'] = self.user_agent
            headers['Accept'] = 'application/json; charset=utf-8'
            headers['Content-type'] = 'content-type: application/json'
            self._headers = headers
        return self._headers

    def get(self, path = '/', params = {}) -> Any:
        return self._client.get(urljoin(self._endpoint, path), params=params, headers=self.headers)

    def put(self, path = '/', params = {}, data = {}) -> Any:
        return self._client.put(urljoin(self._endpoint, path), params=params, headers=self.headers, json=data)

    def post(self, path = '/', params = {}, data = {}) -> Any:
        return self._client.post(urljoin(self._endpoint, path), params=params, headers=self.headers, json=data)

    def delete(self, path = '/', params = {}) -> Any:
        return self._client.delete(urljoin(self._endpoint, path), params=params, headers=self.headers)
