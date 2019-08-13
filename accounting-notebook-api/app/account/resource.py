from flask import jsonify, request
from .schema import account_schema
from marshmallow import ValidationError

def register(app):

    @app.route('/', methods=['GET'])
    def get_balance():
        result = account_schema.dump(app.account)
        return jsonify(result.data)

