from datetime import datetime


class VaccinesGenerator:

    def __init__(self, connection):
        self.connection = connection

    def register_vaccination(self, name, pet):
        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO vaccination (pet_id, name, date, status) VALUES (%s, %s, %s, 'PENDING')",
            (pet[0], name, datetime.now()),
        )
        self.connection.commit()
