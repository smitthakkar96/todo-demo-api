import os


class Settings(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/flask_todo.db'
    DEBUG = True
    SECRET_KEY = 'dev'


class ProductionSettings(Settings):

    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_CHARCOAL_URL')
    DEBUG = False
    SECRET_KEY = os.environ.get('FLASK_TODO_SECRET_KEY')
