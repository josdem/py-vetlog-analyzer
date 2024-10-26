from py_vetlog_analyzer.database_connector import Connector
from datetime import datetime


class VaccinesGenerator:

    def register_vaccination(name, pet):
        connection = Connector().get_connector()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO vaccination (pet_id, name, date, status) VALUES (%s, %s, %s, 'PENDING')",
            (pet[0], name, datetime.now()),
        )
        connection.commit()
