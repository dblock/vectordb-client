from abc import ABC, abstractmethod
from typing import Dict

class Credentials(ABC):
    # todo: this needs to become some kind of apply/filter on a connection
    @abstractmethod
    def headers(self) -> Dict:
        pass
