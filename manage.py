from flask_migrate import MigrateCommand
from flask_script import Manager
import unittest

from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@manager.command
def run():
    app.run(host="0.0.0.0", port=5000)


@manager.command
def test():
    """Runs the unit tests"""
    tests = unittest.TestLoader().discover("main/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
