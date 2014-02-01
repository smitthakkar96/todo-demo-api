import os
from flask import Flask
# import flask.ext.restless
from flask.ext import restful
from settings import Settings, ProductionSettings
from todo.models import db
from todo.resources import TodoResource


app = Flask(__name__)
db.init_app(app)

# manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
# manager.create_api(Todo, methods=['GET', 'PUT', 'POST', 'DELETE'], collection_name='todos')

todoApi = restful.Api(app)
todoApi.add_resource(TodoResource, '/api/todos')

# Settings based on environment
if os.environ.get('FLASK_TODO_PRODUCTION'):
    app.config.from_object(ProductionSettings)
else:
    app.config.from_object(Settings)


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = \
        'Accept, Content-Type, Origin, X-Requested-With'
    return response


def create_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    if os.environ.get('FLASK_TODO_PRODUCTION'):
        app.run(host='0.0.0.0')
    else:
        app.run()
