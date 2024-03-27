import streamlit as st
import time
import winsound

class CountdownTimer:
    def __init__(self, duration, timer_placeholder):
        self.duration = duration
        self.timer_placeholder = timer_placeholder

    def start(self):
        for x in range(self.duration, 0, -1):
            seconds = x % 60
            minutes = (x // 60) % 60
            hours = x // 3600
            timer_text = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.timer_placeholder.write(timer_text)
            time.sleep(1)

class ExerciseManager:
    def __init__(self, num_exercises, rounds_per_exercise, round_duration, rest_between_rounds, rest_between_exercises):
        self.num_exercises = num_exercises
        self.rounds_per_exercise = rounds_per_exercise
        self.round_duration = round_duration
        self.rest_between_rounds = rest_between_rounds
        self.rest_between_exercises = rest_between_exercises

    def do_exercise(self):
        exercice_placeholder = st.empty()
        for exercise_num in range(1, self.num_exercises + 1):
            exercice_placeholder.header(f"Exercise {exercise_num}:")
            self.play_sound("souds/start.wav")  # Play start sound only at the beginning of each exercise
            for round_num in range(1, self.rounds_per_exercise + 1):
                round_placeholder = st.empty()  # Create empty placeholder for round content
                round_placeholder.subheader(f"Round {round_num}:")
                timer_placeholder = st.empty()  # Create empty placeholder for round timer
                timer = CountdownTimer(self.round_duration, timer_placeholder)
                timer.start()
                if round_num < self.rounds_per_exercise:
                    round_placeholder.empty()  # Clear previous round content
                    timer_placeholder.empty()  # Clear previous timer
                    self.countdown_rest(self.rest_between_rounds, f"Rest between rounds: ")
                if round_num == self.rounds_per_exercise:
                    round_placeholder.empty()
                    subheader_placeholder = st.empty()
                    timer_placeholder.empty()
            if exercise_num < self.num_exercises:
                subheader_placeholder = st.empty()  # Create empty placeholder for subheader
                subheader_placeholder.subheader("Rest between exercises:")  # Display subheader
                timer_placeholder = st.empty()  # Create empty placeholder for rest timer
                timer = CountdownTimer(self.rest_between_exercises, timer_placeholder)
                timer.start()
                subheader_placeholder.empty()  # Clear subheader after timer completion
                timer_placeholder.empty()  # Clear rest timer after completion
        
        exercice_placeholder = st.empty()

        # Clear the last round subheader and last "Rest between exercises" subheader
        st.empty()
        st.empty()

    def countdown_rest(self, duration, message):
        self.play_sound("souds/rest.wav")
        subheader_placeholder = st.empty()  # Create empty placeholder for subheader
        subheader_placeholder.subheader(message)  # Display subheader
        timer_placeholder = st.empty()  # Create empty placeholder for rest timer
        for x in range(duration, 0, -1):
            seconds = x % 60
            minutes = (x // 60) % 60
            hours = x // 3600
            timer_text = f"{hours:02}:{minutes:02}:{seconds:02}"
            timer_placeholder.write(timer_text)  # Update timer value
            time.sleep(1)
        timer_placeholder.empty()  # Clear rest timer after completion
        subheader_placeholder.empty()  # Clear subheader after timer completion

    def play_sound(self, sound_file):
        winsound.PlaySound(sound_file, winsound.SND_FILENAME)


def main():
    st.markdown("<h2 style='text-align: center;color: #AA0000;'>HIIT-TIMER APPLICATION</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Welcome to the HIIT Timer app! Take your workouts to the next level with customizable intervals and real-time feedback. Maximize your efficiency and achieve your fitness goals faster than ever before. Let's get started!</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ED2939;'>Start your journey to a stronger, fitter you today with the HIIT Timer App! and Stay tuned as we explore integrating AI technology to revolutionize your training experience. Your fitness journey is about to reach new heights!</p>", unsafe_allow_html=True)
    # the timer
    st.markdown("<h1>Timer</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h1 style='text-align: center; color: #C60C30;'>Workout Parameters</h1>", unsafe_allow_html=True)
    num_exercises = st.sidebar.number_input("Number of exercises:", min_value=1, step=1)
    rounds_per_exercise = st.sidebar.number_input("Rounds per exercise:", min_value=1, step=1)
    round_duration = st.sidebar.number_input("Round duration (seconds):", min_value=1, step=1)
    rest_between_rounds = st.sidebar.number_input("Rest between rounds (seconds):", min_value=0, step=1)
    rest_between_exercises = st.sidebar.number_input("Rest between exercises (seconds):", min_value=0, step=1)

    start_button = st.sidebar.button("Start Exercise")
    
    if start_button:
        exercise_manager = ExerciseManager(num_exercises, rounds_per_exercise, round_duration, rest_between_rounds, rest_between_exercises)
        exercise_manager.do_exercise()
        st.success("ALL EXERCISES ARE COMPLETED!")
        winsound.PlaySound("souds/success.wav", winsound.SND_FILENAME)

if __name__ == "__main__":
    main()
