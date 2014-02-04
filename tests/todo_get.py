from tests.base import TodoBaseTestCase


class TodoGetTestCase(TodoBaseTestCase):

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
        assert(str(todo.id) in response.data)
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

        assert(str(todo1.id) in response.data)
        assert(todo1.task in response.data)
        assert(unicode(todo1.is_done).lower() in response.data)

        assert(str(todo2.id) in response.data)
        assert(todo2.task in response.data)
        assert(unicode(todo2.is_done).lower() in response.data)

        assert(str(todo3.id) in response.data)
        assert(todo3.task in response.data)
        assert(unicode(todo3.is_done).lower() in response.data)
