import mysql.connector

def connect():
    print("Connecting to database")
    return mysql.connector.connect(
        host="localhost",
        user="vetlogUser",
        password="vetlogDB",
        database="vetlog")