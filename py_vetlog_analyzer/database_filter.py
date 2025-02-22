import os
from py_vetlog_analyzer.filter_username import filter_username
from py_vetlog_analyzer.suspicious_username import is_suspicious_username
from py_vetlog_analyzer.user_remover import Remover
from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.logger import Logger
from dotenv import load_dotenv

load_dotenv()


class Filter:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()
        self.logger = Logger("Filter")
        self.factor = os.getenv("FACTOR")

    def filter_users(self, column: int):
        count = 0
        self.logger.info("Finding usernames")
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        self.logger.info("Total users found: %d", len(result))
        remover = Remover(self.connection)
        for row in result:
            if not filter_username(row[column], self.factor):
                count += 1
                self.logger.info(
                    "No valid user found: id:"
                    + str(row[0])
                    + " username:"
                    + row[10]
                    + "first_name:"
                    + row[11]
                    + "last_name:"
                    + row[12]
                    + " email:"
                    + row[5]
                )
                remover.remove_user(row[0])
        self.logger.info("Invalid users found: %d", count)
        self.connection.close()
        return count

    def suspicious_usernames(self):
        count = 0
        self.logger.info("Finding usernames")
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        self.logger.info("Total users found: %d", len(result))
        for row in result:
            if is_suspicious_username(row[12]):
                count += 1
                self.logger.info(
                    "Suspicious user: id:"
                    + str(row[0])
                    + " username:"
                    + row[10]
                    + "first_name:"
                    + row[11]
                    + "last_name:"
                    + row[12]
                    + " email:"
                    + row[5]
                )
        self.logger.info("Suspicious users found: %d", count)
        self.connection.close()
        return count
