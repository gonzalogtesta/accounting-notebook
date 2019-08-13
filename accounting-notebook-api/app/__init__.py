import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from app.base import error_handlers
from app.account.model import Account
from app.transactions.resource import register as transaction_resource
from app.account.resource import register as account_resource

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    ma = Marshmallow(app)
    app.ma = ma
    app.account = Account()
    CORS(app, resources={r"/*": {"origins": "*"}})
    error_handlers.register_error_handlers(app)
    transaction_resource(app)
    account_resource(app)


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

    return app