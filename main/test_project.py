import unittest
import sys

from app import create_app, GithubUsers


class ProjectTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_index_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome to Github project', result.data)

    def test_model(self):
        model = GithubUsers(
            id=10, username='username', avatar_url='some image link', type='USER', url='some url')
        self.assertEqual(model.id, 10)
        self.assertEqual(model.avatar_url, 'some image link')
        self.assertEqual(model.username, 'username')
        self.assertEqual(model.type, 'USER')
        self.assertEqual(model.url, 'some url')
