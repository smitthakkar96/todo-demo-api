import json
from tests.base import TodoBaseTestCase


class TodoPostTestCase(TodoBaseTestCase):

    def test_todos_post_successful(self):
        """
        Ensure that a valid POST request to /api/todos
        will create a new Todo record.
        """
        post_data = {
            "todo": {
                "task": "Morning yoga practice",
                "is_done": False
            }
        }

        headers = {'Content-Type': 'application/json'}

        response = self.app.post('/api/todos', data=json.dumps(post_data), headers=headers)
        assert(response.status_code == 201)
        assert(post_data["todo"]["task"] in response.data)
        assert(str(post_data["todo"]["is_done"]).lower() in response.data)

    def test_todos_post_invalid(self):
        """
        Ensure that invalid POST requests to /api/todos
        will get a 400 error code response.
        """
        post_data = {
            "todo": {
                "is_done": False
            }
        }

        headers = {'Content-Type': 'application/json'}

        response = self.app.post('/api/todos', data=json.dumps(post_data), headers=headers)
        assert(response.status_code == 400)
