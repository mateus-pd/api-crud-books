from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mateus/Projetos/python/crud-books/tmp/crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Config App
    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    # Configure Routes
    from .books import bp_books
    app.register_blueprint(bp_books)

    return app