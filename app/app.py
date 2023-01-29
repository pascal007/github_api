import os
import sqlite3
from sqlite3 import OperationalError
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.secret_key = '678oyu098ij9i0ipkikp'
# os.mkdir('main')
# os.mkdir('main/database')
db_name = 'github_users.db'
db_path = os.path.join(os.path.dirname(__file__) + '/main/database', db_name)
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db = SQLAlchemy(app)


def get_or_create_conn():
    """ This checks and creates a database connection"""
    try:
        conn = sqlite3.connect(f'main/database/{db_name}')
    except Exception:
        os.mkdir('main')
        os.mkdir('main/database')
        conn = sqlite3.connect(f'main/database/{db_name}')

    if conn is not None:
        return conn


class GithubUsers(db.Model):
    __tablename__ = "github_users"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(30), unique=True)
    avatar_url = db.Column("avatar_url", db.String(100))
    type = db.Column("type", db.String(20))
    url = db.Column("url", db.String(100), unique=True)
    created = db.Column(db.Date, default=datetime.utcnow, nullable=True)

    def __init__(self, id, username, avatar, typ, url):
        self.id = id
        self.username = username
        self.avatar_url = avatar
        self.type = typ
        self.url = url


@app.route("/users")
def users():
    page = request.args.get('page')
    per_page = request.args.get('pagination')

    page = int(page) if (page and page.isdigit()) else 1
    per_page = int(per_page) if (per_page and per_page.isdigit()) else 25
    users = GithubUsers.query.order_by()
    pages = users.paginate(page=page, per_page=per_page)

    return render_template('users.html', users=users, pages=pages)


if __name__ == '__main__':
    app.run(debug=True)


















#
#
# DATABASE_NAME = "github_users.db"
# CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS users (
#                         id integer PRIMARY KEY,
#                         username text NOT NULL,
#                         avatar_url text NOT NULL,
#                         type text NOT NULL,
#                         url text NOT NULL,
#                         created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
#                         );"""
#
#
#
#
#
# def get_or_create_conn(database_name):
#     """ This checks and creates a database connection"""
#     try:
#         conn = sqlite3.connect(f'main/database/{database_name}')
#     except OperationalError:
#         os.mkdir('main')
#         os.mkdir('main/database')
#         conn = sqlite3.connect(f'main/database/{database_name}')
#
#     if conn is not None:
#         return conn
#
#
# def create_table(conn, sql_statement):
#     """This creates database table after connection has been established"""
#     if conn:
#         cursor = conn.cursor()
#         cursor.execute(sql_statement)
#         conn.close()
#         return True
#
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
#

#
#
