from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.logger import Logger


class Remover:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()
        self.logger = Logger("Filter")

    def remove_user(self, id: int):
        self.logger.info("Deleting user with id: %d", id)
        self.cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        self.connection.commit()
        self.connection.close()
