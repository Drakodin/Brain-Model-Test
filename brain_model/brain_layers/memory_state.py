# Include module import of psycopg2 for PostgreSQL or SQL Server
import psycopg2
class MemoryState:
    data_adapter = psycopg2.Adapter()
    init = False
    def __init__(self):
        self.init = True

    def checkMem(self, input):
        if self.data_adapter.getquoted() == input:
            return self.data_adapter.getquoted()

    def get_memory(self):
        return self.data_adapter