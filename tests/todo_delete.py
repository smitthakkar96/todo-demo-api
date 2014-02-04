from tests.base import TodoBaseTestCase


class TodoDeleteTestCase(TodoBaseTestCase):

    def test_todos_delete_successful(self):
        """
        Ensure that a DELETE request to /api/todos/<id>
        will remove the object from the database.
        """
        todo = self.create_todo('Feed the panda', False)
        response = self.app.delete('/api/todos/' + str(todo.id))
        assert(response.status_code == 200)
        assert('{}\n' in response.data)

    def test_todos_delete_not_found(self):
        """
        Ensure that DELETE request to /api/todos/<id>
        will result in a status code of 404 when an object
        with that ID does NOT exist.
        """
        response = self.app.delete('/api/todos/99000000')
        assert(response.status_code == 404)
