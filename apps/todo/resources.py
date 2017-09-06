from flask.ext.restful import abort, fields, marshal
from flask.ext import restful
from flask import g, request
from .models import Todo


class TodoResource(restful.Resource):

    def get_resource_fields(self):
        return {
            'id': fields.Integer,
            'task': fields.String,
            'is_done': fields.Boolean,
        }


    def get_all(self, api_key):
        todos = Todo.query.filter_by(api_key=api_key)
        # TODO: Should probably add pagination...
        for todo in todos:
            yield marshal(todo, self.get_resource_fields())

    def get(self):
        if "api_key" not in request.headers:
            return {
                "error": "api_key is missing"
            }, 400
        todo_list = list(self.get_all(request.headers.get('api_key')))
        return {
            'todos': todo_list
        }

    def post(self):

        todo_json = request.json
        try:
            # TODO: Should handle "data-validation" better
            # ...couldn't get it to work with reqparse.
            if 'api_key' not in request.headers:
                return {
                    "error": "api_key is missing"
                }, 400
            todo = Todo(todo_json['task'], todo_json['is_done'], request.headers.get('api_key'))
            g.db.session.add(todo)
            g.db.session.commit()
        except Exception as e:
            print(e)
            abort(400)

        return {
            'todo': marshal(todo, self.get_resource_fields())
        }, 201

    def put(self, todo_id=None):
        if not todo_id:
            return abort(404)

        todo = Todo.query.get(todo_id)

        if not todo:
            abort(404)

        todo_json = request.get_json()
        try:
            # TODO: Again... better error handling required.
            # This will do as a temp. fix for now.
            todo_data = todo_json["todo"]
            todo.is_done = todo_data['is_done']
            todo.task = todo_data['task']
            g.db.session.commit()
        except:
            abort(400)

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
