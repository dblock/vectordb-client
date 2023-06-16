from abc import ABC

class Index(ABC):
    @property
    def name(self) -> str:
        return self._name
    
    def __init__(self, name: str) -> None:
        self._name = name
