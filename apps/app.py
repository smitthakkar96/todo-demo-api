import os
from flask import Flask
from flask.ext import restful
from settings import Settings, ProductionSettings
from todo.models import db
from todo.resources import TodoResource

app = Flask(__name__)
db.init_app(app)
todoApi = restful.Api(app)
todoApi.add_resource(TodoResource, '/')

# Settings based on environment
if os.environ.get('FLASK_TODO_PRODUCTION'):
    app.config.from_object(ProductionSettings)
else:
    app.config.from_object(Settings)


def create_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run()
