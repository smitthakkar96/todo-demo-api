from flask.ext.script import Manager
from apps.app import app, db

manager = Manager(app)


@manager.command
def test():
    import unittest
    suite = unittest.TestLoader().discover("tests", pattern="*.py")
    unittest.TextTestRunner().run(suite)


@manager.command
def createdb():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    manager.run()
