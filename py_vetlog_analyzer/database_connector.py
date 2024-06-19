import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Connector:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DATABASE"),
        )

    def get_connector(self):
        return self.connection
