from timer import Timer

class Workout:
    def __init__(self, exercises=[], rounds_per_exercise=3, round_duration=30, break_time_between_rounds=10, break_time_between_exercises=20):
        self.exercises = exercises
        self.rounds_per_exercise = rounds_per_exercise
        self.round_duration = round_duration
        self.break_time_between_rounds = break_time_between_rounds
        self.break_time_between_exercises = break_time_between_exercises
        self.current_exercise_index = 0
        self.current_round = 0
        self.timer = Timer(round_duration, self._timer_callback)
        self.timer_running = False

    def _timer_callback(self):
        if self.current_round < self.rounds_per_exercise:
            self.current_round += 1
            self._start_round()
        else:
            self.current_exercise_index += 1
            self.current_round = 1
            print("Round finished!")

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def start_workout(self):
        self.timer.start()
        self.timer_running = True
        self.current_exercise_index = 0
        self.current_round = 1
        self._start_round()

    def _start_round(self):
        if self.current_exercise_index < len(self.exercises):
            exercise = self.exercises[self.current_exercise_index]
            print(f"Round {self.current_round}: {exercise.name} - {self.round_duration} seconds")

    def pause_workout(self):
        self.timer.pause()
        self.timer_running = False
        print(f"Pause {self.current_round}:{self.break_time_between_rounds} seconds")

    def resume_workout(self):
        self.timer.resume()
        self.timer_running = True

    def reset_workout(self):
        self.timer.reset()
        self.timer_running = False
        self.current_exercise_index = 0
        self.current_round = 0

    def is_running(self):
        return self.timer_running
