import os
import mox
import mysql.connector
from py_vetlog_analyzer.database_connector import *


class FixedTest(mox.MoxTestBase):
    def test_mox_database_connector(self):
        connection = self.mox.CreateMockAnything()
        self.mox.StubOutWithMock(mysql.connector, "connect")

        mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("VETLOG_USER"),
            password=os.getenv("VETLOG_PASSWORD"),
            database=os.getenv("DATABASE"),
        ).AndReturn(connection)

        self.mox.ReplayAll()
        connector = Connector()

        assert connector.get_connector() == connection
