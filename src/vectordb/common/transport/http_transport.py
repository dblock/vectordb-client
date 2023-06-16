from typing import Any, Dict
from httpx import Client, HTTPTransport
from vectordb.common.transport.transport import Transport
from vectordb.common.auth.credentials import Credentials
from urllib.parse import urljoin, urlparse

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
        self._client = Client(verify=False)
        self._credentials = credentials
        self._headers = None

    @property
    def headers(self) -> Dict:
        if not self._headers:
            headers = self._credentials.headers.copy()
            headers['User-agent'] = self.user_agent
            headers['Accept'] = 'application/json; charset=utf-8'
            self._headers = headers
        return self._headers

    def get(self, namespace = None, path = '/', params = {}) -> Any:
        return self._client.get(self._resolve(namespace=namespace, path=path), params=params, headers=self.headers)

    def put(self, namespace = None, path = '/', params = {}, data = {}) -> Any:
        return self._client.put(self._resolve(namespace=namespace, path=path), params=params, headers=self.headers, json=data)

    def post(self, namespace = None, path = '/', params = {}, data = None) -> Any:
        headers_with_content_type = self.headers | { 'content-type' : 'application/json; charset=utf-8' }
        if isinstance(data, str):
            return self._client.post(self._resolve(namespace=namespace, path=path), params=params, headers=headers_with_content_type, data=data)
        else:
            return self._client.post(self._resolve(namespace=namespace, path=path), params=params, headers=headers_with_content_type, json=data)

    def delete(self, namespace = None, path = '/', params = {}) -> Any:
        return self._client.delete(self._resolve(namespace=namespace, path=path), params=params, headers=self.headers)
    
    def _resolve(self, namespace = None, path = '/') -> str:
        if not namespace:
            return urljoin(self._endpoint, path)
        else:
            parsed = urlparse(self._endpoint)
            parsed = parsed._replace(netloc=f'{namespace}.{parsed.netloc}', path=path)
            return parsed.geturl()