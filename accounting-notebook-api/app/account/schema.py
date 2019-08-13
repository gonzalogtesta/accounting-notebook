from marshmallow import Schema, fields, pprint, post_load
from .model import Account
from app.transactions.schema import transaction_schema

class AccountSchema(Schema):
    balance = fields.Float()
    transactions = fields.Nested(transaction_schema, many=True)

    @post_load
    def make_transaction(self, data, **kwargs):
        return Account(**data)

account_schema = AccountSchema()