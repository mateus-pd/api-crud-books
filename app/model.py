from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Integer)
    book = db.Column(db.String(200))
    author = db.Column(db.String(200))