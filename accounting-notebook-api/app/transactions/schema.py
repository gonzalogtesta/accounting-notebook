from marshmallow import Schema, fields, pprint, post_load
from marshmallow_enum import EnumField
from app.operations.model import Operations
from .model import Transaction


class TransactionSchema(Schema):
    id = fields.Str(dump_only=True)
    type = EnumField(Operations)
    amount = fields.Float()
    description = fields.Str()
    effectiveDate = fields.DateTime(dump_only=True, attribute='effective_date')

    @post_load
    def make_transaction(self, data, **kwargs):
        return Transaction(**data)

transaction_schema = TransactionSchema()