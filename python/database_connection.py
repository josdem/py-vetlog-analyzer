import mysql.connector
from python.filter_username import *

def connect():
    print("Connecting to database")
    return mysql.connector.connect(
        host="localhost",
        user="vetlogUser",
        password="vetlogDB",
        database="vetlog")

def filter_usernames():
    count = 0
    print("Finding usernames")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    print("first row", result[0])
    print("Total users found: ", len(result))
    for row in result:
        if not filter_username(row[12]):
            count += 1
            print("No valid username: id", row[0], "username:", row[12], "first_name: ", row[7], "last_name: ", row[8], "email:", row[5])
    print("Invalid users found: ", count)
    connection.close()
    return count