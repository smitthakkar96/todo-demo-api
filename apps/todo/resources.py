from flask.ext import restful
# from .models import Todo
# from flask_restful.utils import cors


class TodoResource(restful.Resource):

    def get(self):
        return {
            'todos': [
                {
                    'id': 1,
                    'task': 'hello there'
                }
            ]
        }

    def post(self):
        return {'status': 'created'}
