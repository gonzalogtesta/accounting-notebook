from app.account.exceptions import NoAvailableFounds, OperationNotImplemented, InvalidTransaction
from werkzeug.exceptions import NotFound

def register_error_handlers(app):

    @app.errorhandler(NoAvailableFounds)
    def no_available_funds(e):
        error = {
            'message': 'No available founds in the account!'
        }
        return error, 400

    @app.errorhandler(OperationNotImplemented)
    def not_valid_operation(e):
        error = {
            'message': 'Operation is not valid!'
        }
        return error, 400

    @app.errorhandler(InvalidTransaction)
    def not_valid_transaction(e):
        error = {
            'message': 'Invalid transaction'
        }
        return error, 400

    @app.errorhandler(NotFound)
    def not_found(e):
        return '', 404

