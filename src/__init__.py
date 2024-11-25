import os

from flask import Flask
from src.database.utils import close_db, connect_db, initialize_models

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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