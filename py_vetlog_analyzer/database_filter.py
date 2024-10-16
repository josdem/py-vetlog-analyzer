from py_vetlog_analyzer.filter_username import filter_username
from py_vetlog_analyzer.suspicious_username import is_suspicious_username
from py_vetlog_analyzer.database_connector import Connector


class Filter:
    def __init__(self):
        self.connection = Connector().get_connector()
        self.cursor = self.connection.cursor()

    def filter_usernames(self):
        count = 0
        print("Finding usernames")
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        print("Total users found: ", len(result))
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
        print("Invalid users found: ", count)
        self.connection.close()
        return count

    def suspicious_usernames(self):
        count = 0
        print("Finding usernames")
        self.cursor.execute("SELECT * FROM user")
        result = self.cursor.fetchall()
        print("Total users found: ", len(result))
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
        print("Suspicious users found: ", count)
        self.connection.close()
        return count
