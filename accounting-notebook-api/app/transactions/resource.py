from flask import jsonify, request, abort
from .schema import transaction_schema
from marshmallow import ValidationError

def register(app):

    @app.route('/transactions/<string:id>', methods=['GET'])
    def get_transactions_by_id(id):
        transaction = next((transaction for transaction in app.account.transactions() if str(transaction.id) == id), None)
        print(transaction)
        print(app.account.transactions)
        if transaction is None:
            abort(404)

        result = transaction_schema.dump(transaction)
        return jsonify(result.data)

    @app.route('/transactions', methods=['GET'])
    def get_transactions():
        result = transaction_schema.dump(app.account.transactions(), many=True)
        return jsonify(result.data)

    @app.route('/transactions', methods=['POST'])
    def create_transaction():
        json_data = request.get_json()
        if not json_data:
            return jsonify({"message": "No input data provided"}), 400

        try:
            data = transaction_schema.load(json_data)
        except ValidationError as err:
            return jsonify(err.messages), 422
        transaction = data.data
        app.account.process(transaction)
        result = transaction_schema.dump(data.data)
        return jsonify(result.data)


