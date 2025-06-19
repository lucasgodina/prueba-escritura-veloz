import time


class Timer:
    def __init__(self):
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = time.time()
        self._end_time = None

    def stop(self):
        if self._start_time is not None:
            self._end_time = time.time()

    def reset(self):
        self._start_time = None
        self._end_time = None

    def elapsed(self) -> float:
        """
        Retorna el tiempo transcurrido en segundos.
        """
        if self._start_time is None:
            return 0.0
        if self._end_time is not None:
            return self._end_time - self._start_time
        return time.time() - self._start_time
