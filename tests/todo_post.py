import json
from tests.base import TodoBaseTestCase


class TodoPostTestCase(TodoBaseTestCase):

    def test_todos_post_successful(self):
        """
        Ensure that a valid POST request to /api/todos
        will create a new Todo record.
        """
        post_data = json.dumps({
            "todo": {
                "task": "Morning yoga practice",
                "is_done": "false"
            }
        })

        # response = self.app.post('/api/todos', data=post_data)
        # import pdb; pdb.set_trace()
        # response = self.app.post('/api/todos', data=post_data)
        # assert(response.status_code == 201)
