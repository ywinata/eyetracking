import time


class Timer:

    def __init__(self):
        self.start = time.perf_counter()
        self.frames = 0

    def update(self):
        self.frames += 1

    @property
    def fps(self):

        elapsed = time.perf_counter() - self.start

        if elapsed == 0:
            return 0.0

        return self.frames / elapsed