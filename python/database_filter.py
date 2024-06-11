from python.filter_username import *
from python.database_connector import *


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
