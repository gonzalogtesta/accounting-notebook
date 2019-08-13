import threading
from .exceptions import NoAvailableFounds, OperationNotImplemented, InvalidTransaction
from app.operations.model import Operations
from app.base.readwritelock import ReadWriteLock

class Account(object):

    def __init__(self):
        self._transactions = []
        self._balance = 0
        self.lock = ReadWriteLock()

    def _credit(self, transaction):

        self.lock.acquire_write()
        try:
            self._balance += transaction.amount
            self._transactions.insert(0, transaction)

        finally:
            self.lock.release_write()

    def _debit(self, transaction):

        self.lock.acquire_write()
        try:
            if self._balance < transaction.amount:
                raise NoAvailableFounds()
            self._balance -= transaction.amount
            self._transactions.insert(0, transaction)
        finally:
            self.lock.release_write()

    def process(self, transaction):

        if transaction is None:
            raise InvalidTransaction()

        if transaction.type == Operations.DEBIT:
            self._debit(transaction)
        elif transaction.type == Operations.CREDIT:
            self._credit(transaction)
        else:
            raise OperationNotImplemented()

    def balance(self):
        try:
            self.lock.acquire_read()
            return self._balance
        finally:
            self.lock.release_read()

    def transactions(self):
        try:
            self.lock.acquire_read()
            return self._transactions
        finally:
            self.lock.release_read()