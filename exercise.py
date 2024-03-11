class Exercise:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"Exercise: {self.name}, Duration: {self.duration}s"

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration

    def set_name(self, name):
        self.name = name

    def set_duration(self, duration):
        self.duration = duration
