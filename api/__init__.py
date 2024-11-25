import os

from flask import Flask
from flask_migrate import Migrate
from api.database.models import db
from api.database.utils import close_db, connect_db, initialize_models

def create_app(test_config=None):
    '''
    Create and configure an instance of the Flask application
    '''
    app = Flask(__name__)
    migrate = Migrate(app, db)

    @app.before_request
    def before_request():
        connect_db()

    @app.teardown_request
    def teardown_request(exception):
        close_db()

    with app.app_context():
        initialize_models()

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, I am working out! 🏋️‍♀️'

    return app
