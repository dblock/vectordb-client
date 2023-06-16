from abc import ABC, abstractmethod
from typing import Any
from vectordb.common.auth.credentials import Credentials

class Transport(ABC):
    @abstractmethod
    def connect(self, credentials: Credentials) -> None:
        pass

    @abstractmethod
    def get(self, path = '/', options = {}, data = None) -> Any:
        pass