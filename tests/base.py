import unittest
from apps.app import app, db
from apps.todo.models import Todo


class FlaskRestfulTestCase(unittest.TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TodoBaseTestCase(FlaskRestfulTestCase):

    def create_todo(self, task_name, task_status):
        todo = Todo(task_name, task_status)
        db.session.add(todo)
        db.session.commit()
        return todo
