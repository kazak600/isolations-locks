import random
import uuid
from datetime import datetime
from pymysql import connect, cursors


def insert_row():
    connection = connect(
        host='localhost', user='admin', password='admin', database='isolations_locks', cursorclass=cursors.DictCursor
    )

    sql_query = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s);"
    with connection.cursor() as cursor:
        password = str(random.randint(1, 99999999))
        user = str(uuid.uuid4())
        birth_date = datetime(1971, 1, 1)
        result = cursor.execute(sql_query, (user, password))
        connection.commit()


insert_row()
