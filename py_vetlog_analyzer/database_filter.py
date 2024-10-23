from py_vetlog_analyzer.filter_username import filter_username
from py_vetlog_analyzer.suspicious_username import is_suspicious_username
from py_vetlog_analyzer.database_connector import Connector
from py_vetlog_analyzer.logger import Logger


class Filter:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()
        self.logger = Logger("Filter")

    def filter_usernames(self):
        count = 0
        self.logger.info("Finding usernames")
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        self.logger.info("Total users found: %d", len(result))
        for row in result:
            if not filter_username(row[12]):
                count += 1
                print(
                    "No valid username: id",
                    row[0],
                    "username:",
                    row[12],
                    "first_name: ",
                    row[7],
                    "last_name: ",
                    row[8],
                    "email:",
                    row[5],
                )
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
                print(
                    "Suspicious username: id",
                    row[0],
                    "username:",
                    row[12],
                    "first_name: ",
                    row[7],
                    "last_name: ",
                    row[8],
                    "email:",
                    row[5],
                )
        self.logger.info("Suspicious users found: %d", count)
        self.connection.close()
        return count
