from flask.ext import restful


class RootResource(restful.Resource):

    def get(self):

        return {
            'Todo API ROOT': {
                'Available CRUD endpoints': [
                    {'name': 'todos', 'url': '/api/todos'}
                ]
            }
        }
