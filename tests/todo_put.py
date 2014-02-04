import json
from tests.base import TodoBaseTestCase


class TodoPutTestCase(TodoBaseTestCase):

    def test_todos_put_successful(self):
        """
        Ensure that a valid PUT request to /api/todos/<id>
        will result in an update of the database record.
        """
        todo = self.create_todo('Run a marthon', False)
        put_data = {
            "todo": {
                "task": todo.task,
                "is_done": True
            }
        }

        headers = {'Content-Type': 'application/json'}
        response = self.app.put('/api/todos/' + str(todo.id), data=json.dumps(put_data), headers=headers)
        assert(response.status_code == 201)
        assert(put_data["todo"]["task"] in response.data)
        assert(str(put_data["todo"]["is_done"]).lower() in response.data)

    def test_todos_put_invalid(self):
        """
        Ensure that invalid PUT request to /api/todos/<id>
        will result in 400 error code.
        """
        todo = self.create_todo('Walk the dog', True)
        invalid_put_data = {
            "task": todo.task,
            "is_done": True
        }
        headers = {'Content-Type': 'application/json'}
        response = self.app.put('/api/todos/' + str(todo.id), data=json.dumps(invalid_put_data), headers=headers)
        assert(response.status_code == 400)
