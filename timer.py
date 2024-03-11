import time
from threading import Thread

class Timer:
    def __init__(self, duration, callback=None):
        self.duration = duration
        self.callback = callback
        self.remaining_time = duration
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self._run)
            self.thread.start()

    def pause(self):
        self.running = False

    def resume(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self._run)
            self.thread.start()

    def reset(self):
        self.running = False
        self.remaining_time = self.duration

    def _run(self):
        while self.remaining_time > 0 and self.running:
            time.sleep(1)
            self.remaining_time -= 1
        if self.callback:
            self.callback()

    def is_running(self):
        return self.running

    def get_remaining_time(self):
        return self.remaining_time
