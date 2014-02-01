from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class APIRoot(restful.Resource):
    def get(self):
        return {'message': 'Welcome to API root.'}

api.add_resource(APIRoot, '/')

if __name__ == '__main__':
    app.run(debug=True)
