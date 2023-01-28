
import os
import sqlite3
from sqlite3 import OperationalError

DATABASE_NAME = "github_users.db"
CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS users (
                        id integer PRIMARY KEY,
                        username text NOT NULL,
                        avatar_url text NOT NULL,
                        type text NOT NULL,
                        url text NOT NULL,
                        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                        );"""


def create_db(database_name):
    """ This checks and creates a database connection"""
    try:
        conn = sqlite3.connect(f'main/database/{database_name}')
    except OperationalError:
        os.mkdir('main')
        os.mkdir('main/database')
        conn = sqlite3.connect(f'main/database/{database_name}')

    if conn is not None:
        return conn


def create_table(conn, sql_statement):
    """This creates database table after connection has been established"""
    if conn:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.close()
        return True


if __name__ == '__main__':
    print()
    # app.run(debug=True)
