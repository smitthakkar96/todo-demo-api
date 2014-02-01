from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255))

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return '<TODO %r>' % self.task
