from flask.ext.restful import abort, fields, marshal
from flask.ext import restful
from .models import Todo


class TodoResource(restful.Resource):

    def get_resource_fields(self):
        return {
            'id': fields.Integer(),
            'task': fields.String,
        }

    def get_one(self, todo_id):
        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        return todo

    def get_all(self):
        todos = Todo.query.all()
        for todo in todos:
            yield marshal(todo, self.get_resource_fields())

    def get(self, todo_id=None):
        if todo_id:
            todo = self.get_one(todo_id)
            return marshal(todo, self.get_resource_fields())
        todo_list = list(self.get_all())
        return {
            'todos': todo_list
        }

    def post(self):
        return {'status': 'created'}
