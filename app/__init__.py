from flask import Flask
from config import config_options
# from flask_bootstrap import Bootstrap


def create_app(config_name):
    """
    Initializing our app
    """

    app = Flask(__name__)

    # Setting up Configurations
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')

    # Registering the blueprint
    from .app2 import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting up the request config
    from .request import configure_request
    configure_request(app)


    return app
