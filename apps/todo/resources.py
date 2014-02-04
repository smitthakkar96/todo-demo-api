from flask.ext.restful import abort, fields, marshal
from flask.ext import restful
from flask import g, request
from .models import Todo


class TodoResource(restful.Resource):

    def __init__(self):
        # TODO: Should add reqparse here
        super(TodoResource, self).__init__()

    def get_resource_fields(self):
        return {
            'id': fields.Integer,
            'task': fields.String,
            'is_done': fields.Boolean,
        }

    def get_one(self, todo_id):
        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        return todo

    def get_all(self):
        todos = Todo.query.all()
        # TODO: Should probably add pagination...
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
        todo_data = request.json['todo']
        # TODO: Should definitely validate this (todo_data) input

        todo = Todo(todo_data['task'], todo_data['is_done'])
        g.db.session.add(todo)
        g.db.session.commit()
        return {
            'todo': marshal(todo, self.get_resource_fields())
        }, 201

    def put(self, todo_id=None):
        if not todo_id:
            return abort(404)

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        todo_data = request.json['todo']
        # TODO: Again, sanitize this data, you fool!

        todo.is_done = todo_data['is_done']
        todo.task = todo_data['task']
        g.db.session.commit()

        return {
            'todo': marshal(todo, self.get_resource_fields())
        }, 201

    def delete(self, todo_id=None):
        if not todo_id:
            return abort(404)

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        g.db.session.delete(todo)
        g.db.session.commit()

        return {}
