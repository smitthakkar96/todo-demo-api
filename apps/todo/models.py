from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255))
    is_done = db.Column(db.Boolean())

    def __init__(self, task, is_done):
        self.task = task
        self.is_done = is_done

    def __repr__(self):
        return '<TODO %r>' % self.task
