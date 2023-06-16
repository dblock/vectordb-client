from abc import ABC, abstractmethod
from typing import Any
from vectordb.common.auth.credentials import Credentials

class Transport(ABC):
    @abstractmethod
    def connect(self, credentials: Credentials) -> None:
        pass

    @abstractmethod
    def get(self, namespace = None, path = '/', params = {}) -> Any:
        pass

    @abstractmethod
    def put(self, namespace = None, path = '/', params = {}, data = {}) -> Any:
        pass

    @abstractmethod
    def post(self, namespace = None, path = '/', params = {}, data = {}) -> Any:
        pass

    @abstractmethod
    def delete(self, namespace = None, path = '/', params = {}) -> Any:
        pass
    