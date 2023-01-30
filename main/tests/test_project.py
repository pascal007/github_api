import json
import os
import unittest
import sys

sys.path.insert(0, "..")
from main.app import create_app, GithubUsers
from main.scripts import seed


class ProjectTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_index_page(self):
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Welcome to Github project", result.data)

    def test_model(self):
        model = GithubUsers(
            id=10,
            username="username",
            avatar_url="some image link",
            type="USER",
            url="some url",
        )
        self.assertEqual(model.id, 10)
        self.assertEqual(model.avatar_url, "some image link")
        self.assertEqual(model.username, "username")
        self.assertEqual(model.type, "USER")
        self.assertEqual(model.url, "some url")

    def test_users_page(self):
        result = self.client.get("/users/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Users Page", result.data)

    def test_database_exist(self):
        db_path = "./database/github_users.sqlite"
        self.assertTrue(os.path.exists(db_path))

    def test_users_profiles(self):
        response = self.client.get("/api/users/profiles")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json.loads(response.data)) > 0)

    def test_seed_script(self):
        result = seed.seed_database()
        self.assertTrue(result)
