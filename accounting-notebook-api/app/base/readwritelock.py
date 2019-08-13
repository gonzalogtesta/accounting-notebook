import threading

class ReadWriteLock:
    """ Allows to lock reads if writes are being performed """

    def __init__(self):
        self._writers_ready = threading.Condition(threading.Lock())
        self._writers = 0

    def acquire_read(self):
        """ Wait while writes are being performed. """
        self._writers_ready.acquire()
        while self._writers > 0:
            self._writers_ready.wait()

    def release_read(self):
        """ Release a read lock. """
        self._writers_ready.release()

    def acquire_write(self):
        """ Acquire a write lock. Blocks until there are no
        write locks. """
        self._writers_ready.acquire()
        while self._writers > 0:
            self._writers_ready.wait()
        try:
            self._writers += 1
        finally:
            self._writers_ready.release()

    def release_write(self):
        """ Release a write lock. """
        self._writers_ready.acquire()
        try:
            self._writers -= 1
            if not self._writers:
                self._writers_ready.notifyAll()
        finally:
            self._writers_ready.release()