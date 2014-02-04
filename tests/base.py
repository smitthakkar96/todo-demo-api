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

    def create_todo(self, task_name, task_status):
        todo = Todo(task_name, task_status)
        db.session.add(todo)
        db.session.commit()
        return todo

    def test_api_root(self):
        """
        Ensure that API root returns OK response code
        and that todos endpoint is listed under available
        CRUD endpoints list.
        """
        response = self.app.get('/')
        assert(response.status_code == 200)
        assert('Available CRUD endpoints' in response.data)
        assert('todos' in response.data)

    def test_todos_get_list_empty(self):
        """
        Ensure that GET request to /api/todos
        list will return an empty OK response.
        """
        response = self.app.get('/api/todos')
        assert(response.status_code == 200)
        assert('todos' in response.data)
        assert('[]' in response.data)

    def test_todos_get_list_single_populated(self):
        """
        Ensure that GET request to /api/todos list
        will return a TODO object.
        """
        todo = self.create_todo('Finish this test', True)
        response = self.app.get('/api/todos')
        assert(response.status_code == 200)
        assert(todo.task in response.data)
        assert(unicode(todo.is_done).lower() in response.data)

    def test_todos_get_list_multiple_populated(self):
        """
        Ensure that GET request to /api/todos list
        will return multiple TODO objects.
        """
        todo1 = self.create_todo('Learn web development', True)
        todo2 = self.create_todo('Work out', True)
        todo3 = self.create_todo('Do the dishes', False)
        response = self.app.get('/api/todos')
        assert(response.status_code == 200)

        assert(todo1.task in response.data)
        assert(unicode(todo1.is_done).lower() in response.data)

        assert(todo2.task in response.data)
        assert(unicode(todo2.is_done).lower() in response.data)

        assert(todo3.task in response.data)
        assert(unicode(todo3.is_done).lower() in response.data)
