import threading
from tests import BaseTestCase


class SerializableDirtyReadsTest(BaseTestCase):

    def test_pg_main(self):
        with self.pg_database:
            with self.pg_database.cursor() as cursor:
                cursor.execute('SELECT * FROM my_table;')

    def test_percona_main(self):
        sql_query = 'SELECT * FROM my_table;'

        with self.percona_database.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
            print(result)
