import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db_path = "github_users.sqlite3"
base_dir = os.path.abspath(os.path.dirname(__file__))
db_uri = "sqlite:///" + os.path.join(base_dir, "database", "github_users.sqlite")

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    os.makedirs("database", exist_ok=True)
    try:
        app.config.from_pyfile("config.cfg")

        if "SQLALCHEMY_DATABASE_URI" in app.config:
            # Database is configured
            app.config["SQLALCHEMY_DATABASE_URI"] = app.config[
                "SQLALCHEMY_DATABASE_URI"
            ]
        else:
            # Database is not configured
            app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    except FileNotFoundError:
        app.config["SQLALCHEMY_DATABASE_URI"] = db_uri

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/users/")
    def users():
        page = request.args.get("page")
        per_page = request.args.get("pagination")
        page = int(page) if (page and page.isdigit()) else 1
        per_page = int(per_page) if (per_page and per_page.isdigit()) else 25
        users_data = GithubUsers.query.order_by()
        pages = users_data.paginate(page=page, per_page=per_page)

        return render_template("users.html", users_data=users_data, pages=pages)

    @app.route("/api/users/profiles", methods=["GET"])
    def users_profile():
        page = request.args.get("page")
        per_page = request.args.get("pagination")
        page = int(page) if (page and page.isdigit()) else 1
        per_page = int(per_page) if (per_page and per_page.isdigit()) else 25
        order_by = request.args.get("order_by")
        username = request.args.get("username")
        primary_key = request.args.get("id")

        match order_by:
            case "id":
                ordering = GithubUsers.id
            case "type":
                ordering = GithubUsers.type
            case _:
                ordering = None

        if not (username or primary_key):
            results = GithubUsers.query.filter().order_by(ordering)
        else:
            results = None
            if username:
                results = GithubUsers.query.filter(username=username).order_by(ordering)
            if primary_key and results:
                results = results.filter(id=primary_key).order_by(ordering)
            elif primary_key and not results:
                results = GithubUsers.query.filter(id=primary_key).order_by(ordering)

        results = results.paginate(page=page, per_page=per_page)

        json_results = [result.as_dict() for result in results.items]

        meta = {
            "page": results.page,
            "pages": results.pages,
            "total_count": results.total,
            "prev_page": results.prev_num,
            "next_page": results.next_num,
            "has_next": results.has_next,
            "has_prev": results.has_prev,
        }

        return jsonify({"data": json_results, "meta": meta})

    return app


class GithubUsers(db.Model):
    __tablename__ = "github_users"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(30), unique=True)
    avatar_url = db.Column("avatar_url", db.String(100))
    type = db.Column("type", db.String(20))
    url = db.Column("url", db.String(100), unique=True)

    def __init__(self, id, username, avatar_url, type, url):
        self.id = id
        self.username = username
        self.avatar_url = avatar_url
        self.type = type
        self.url = url

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar_url": self.avatar_url,
            "type": self.type,
            "url": self.url,
        }
