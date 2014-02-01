import os
from flask import Flask
from settings import Settings, ProductionSettings
from apps.todo.models import db

app = Flask(__name__)
db.init_app(app)

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
