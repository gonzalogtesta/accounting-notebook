import pytest
from app.account.model import Account
from app.transactions.model import Transaction
from app.operations.model import Operations
from app.account.exceptions import NoAvailableFounds, OperationNotImplemented, InvalidTransaction

def test_account_without_operations():
    account = Account()
    assert account.balance() == 0, "Should be 0"
    assert account.transactions() is not None, "Should not be none"
    assert isinstance(account.transactions(), list), "Should be a list"
    assert len(account.transactions()) == 0, "Should be an empty list"

def test_add_credit_to_account():
    account = Account()
    transaction = Transaction()
    transaction.type = Operations.CREDIT
    transaction.amount = 50
    account.process(transaction)
    assert account.balance() == 50, "Should be 50"
    assert len(account.transactions()) == 1, "Should not be empty"

def test_add_debit_to_account():
    account = _account_with_amount(100)
    transaction = Transaction()
    transaction.type = Operations.DEBIT
    transaction.amount = 50
    account.process(transaction)
    assert account.balance() == 50, "Should be 50"
    assert len(account.transactions()) == 2, "Should be 2"

def test_debit_without_balance():
    account = Account()
    transaction = Transaction()
    transaction.type = Operations.DEBIT
    transaction.amount = 50
    with pytest.raises(NoAvailableFounds):
        account.process(transaction)
    assert account.balance() == 0, "Should be 0"

def test_account_with_invalid_transaction_type():
    account = Account()
    transaction = Transaction()
    transaction.type = 'INVALID'
    transaction.amount = 50
    with pytest.raises(OperationNotImplemented):
        account.process(transaction)

    assert account.balance() == 0, "Should be 0"

def test_account_with_none_transaction_type():
    account = Account()
    transaction = Transaction()
    transaction.type = None
    transaction.amount = 50
    with pytest.raises(OperationNotImplemented):
        account.process(transaction)

    assert account.balance() == 0, "Should be 0"

def test_account_with_invalid_transaction():
    account = Account()
    with pytest.raises(InvalidTransaction):
        account.process(None)

    assert account.balance() == 0, "Should be 0"

def _account_with_amount(amount):
    account = Account()
    transaction = Transaction()
    transaction.type = Operations.CREDIT
    transaction.amount = amount
    account.process(transaction)

    return account