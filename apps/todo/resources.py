from flask.ext import restful


class TodoResource(restful.Resource):

    def get(self):
        return {'todo': 'list'}
