import time

class Timer:
    def __init__(self, label=None):
        self.label = label
        self.elapsed = None

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.perf_counter()
        self.elapsed = end - self._start  # tiempo en segundos
        return False

