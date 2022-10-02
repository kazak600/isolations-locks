from unittest import TestCase
from psycopg2 import connect as pg_connect
from pymysql import connect as mysql_connect
from pymysql import cursors


class BaseTestCase(TestCase):

    def setUp(self) -> None:
        db_name = 'isolations_locks'
        user = 'admin'
        password = 'admin'

        self.pg_database = pg_connect(dsn=f'postgresql://{user}:{password}@localhost:5432/{db_name}')
        self.percona_database = mysql_connect(
            host='localhost', user=user, password=password, database=db_name, cursorclass=cursors.DictCursor
        )

    def tearDown(self) -> None:
        self.pg_database.close()
        self.percona_database.close()
