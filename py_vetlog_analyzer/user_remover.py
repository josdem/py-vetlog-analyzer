from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.logger import Logger


class Remover:
    def __init__(self, id: int):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()
        self.logger = Logger("Filter")
        self.userId = id

    def remove_user(self):
        self.logger.info("Deleting user with id: %d", self.userId)
        self.cursor.execute("DELETE FROM user WHERE id = %d", (self.userId,))
        self.connection.commit()
        self.connection.close()
