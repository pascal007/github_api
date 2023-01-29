from app import db


class GithubUsers(db.Model):
    __tablename__ = "github_users"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(30), unique=True)
    avatar_url = db.Column("avatar_url", db.String(100))
    type = db.Column("type", db.String(20))
    url = db.Column("url", db.String(100), unique=True)

    def __init__(self, id, username, avatar, typ, url):
        self.id = id
        self.username = username
        self.avatar_url = avatar
        self.type = typ
        self.url = url

    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar_url": self.avatar_url,
            "type": self.type,
            "url": self.url
        }
