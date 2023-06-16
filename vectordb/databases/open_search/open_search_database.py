from vectordb.common.databases.database import Database
from vectordb.common.databases.indices import Indices

class OpenSearchDatabase(Database):
    @property
    def indices(self) -> Indices:
        pass
    