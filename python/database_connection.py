import os
import mysql.connector
from python.filter_username import *
from dotenv import load_dotenv

load_dotenv()

def connect():
    print("Connecting to database")
    return mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'))

def filter_usernames():
    count = 0
    print("Finding usernames")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    print("Total users found: ", len(result))
    for row in result:
        if not filter_username(row[12]):
            count += 1
            print("No valid username: id", row[0], "username:", row[12], "first_name: ", row[7], "last_name: ", row[8], "email:", row[5])
    print("Invalid users found: ", count)
    connection.close()
    return count