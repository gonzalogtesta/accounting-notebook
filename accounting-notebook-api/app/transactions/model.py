import uuid
from datetime import datetime

class Transaction(object):

    def __init__(self, **kwargs):
        if kwargs.get('id') is None:
            self.id = uuid.uuid4()
            self.effective_date = datetime.now()
        self.__dict__.update(kwargs)
