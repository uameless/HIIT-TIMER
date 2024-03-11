import streamlit as st
from workout import Workout
from timer import Timer
from exercise import Exercise

def main():
    st.title("HIIT Timer App")

    # Sidebar for workout settings
    st.sidebar.header("Workout Settings")
    num_exercises = st.sidebar.number_input("Number of Exercises", min_value=1, value=3)
    rounds_per_exercise = st.sidebar.number_input("Rounds per Exercise", min_value=1, value=3)
    round_duration = st.sidebar.number_input("Round Duration (seconds)", min_value=1, value=30)
    break_time_between_rounds = st.sidebar.number_input("Break Time between Rounds (seconds)", min_value=1, value=10)
    break_time_between_exercises = st.sidebar.number_input("Break Time between Exercises (seconds)", min_value=1, value=20)

    # Create exercises
    exercises = []
    for i in range(num_exercises):
        exercise_name = st.text_input(f"Exercise {i+1} Name", f"Exercise {i+1}")
        exercises.append(Exercise(exercise_name, round_duration))
    
    workout = Workout(exercises, rounds_per_exercise, round_duration, break_time_between_rounds, break_time_between_exercises)

    if st.button("Start Workout"):
        st.write("Workout Started!")
        print("Workout Started!")
        workout.start_workout()

    if st.button("Pause Workout"):
        st.write("Workout Paused!")
        workout.pause_workout()

    if st.button("Resume Workout"):
        st.write("Workout Resumed!")
        workout.resume_workout()

    if st.button("Reset Workout"):
        st.write("Workout Reset!")
        workout.reset_workout()

    # Display workout status
    if workout.is_running():
        st.write(f"Current Exercise: {workout.current_exercise_index + 1}/{len(exercises)}")
        st.write(f"Current Round: {workout.current_round}/{rounds_per_exercise}")
        st.write(f"Time Remaining: {workout.timer.get_remaining_time()} seconds")

if __name__ == "__main__":
    main()