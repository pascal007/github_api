import requests
import sqlite3
from sqlite3 import OperationalError

API_URL = "https://api.github.com/users"
response = requests.get(url=API_URL).json()


def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect('../main/database/github_users.db')
    except Exception as e:
        print('Data not saved. Database connection error')
        print(e)
    return conn


data = [
    (data['id'], data['login'], data['avatar_url'], data['type'], data['url']) for data in response]

conn = get_db_connection()
if conn:
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO users (id, username, avatar_url, type, url) values (%d,%s,%s,%s,%s)", data)
    conn.commit()
    print('Successfully saved')





#
# print(data)
# print(len(data))
