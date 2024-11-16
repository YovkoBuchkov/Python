from user import User
from exercise import Exercise
from workout import Workout
from progress import ProgressTracker


def show_menu():
    menu = {
        "1": "Update Weight",
        "2": "Update Goal",
        "3": "Log Workout",
        "4": "Display Info",
        "5": "View Exercises",
        "6": "Create/Modify Workouts",
        "7": "Track Progress",
        "8": "Exit"
    }
    print("\nMenu:")
    for key, value in menu.items():
        print(f"{key}. {value}")


name = input("Enter name: ")
age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
goal = input("Enter fitness goal: ")

user1 = User(name, age, weight, height, goal)
progress_tracker = ProgressTracker(user1)
exercise_library = [
    Exercise("Squat", "A lower body exercise.", "Moderate"),
    Exercise("Push-Up", "An upper body exercise.", "Easy"),
    Exercise("Lunge", "A lower body exercise.", "Hard")
]

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        new_weight = float(input("Enter new weight: "))
        user1.update_weight(new_weight)
        print("Weight updated successfully.")
    elif choice == "2":
        new_goal = input("Enter new goal: ")
        user1.update_goal(new_goal)
        print("Goal updated successfully.")
    elif choice == "3":
        workout = input("Enter workout details: ")
        user1.log_workout(workout)
        print("Workout logged successfully.")
    elif choice == "4":
        print(user1.display_info())
    elif choice == "5":
        for exercise in exercise_library:
            print(exercise.display_exercise())
    elif choice == "6":
        workout_name = input("Enter workout name: ")
        workout = Workout(workout_name)
        while True:
            exercise_name = input("Enter exercise name (or 'done' to finish): ")
            if exercise_name == "done":
                break
            sets = int(input("Enter number of sets: "))
            reps = int(input("Enter number of reps: "))
            rest_time = int(input("Enter rest time (seconds): "))
            exercise = next((ex for ex in exercise_library if ex.name == exercise_name), None)
            if exercise:
                workout.add_exercise(exercise, sets, reps, rest_time)
            else:
                print(f"Exercise '{exercise_name}' not found in library.")
        workout.view_workout()
    elif choice == "7":
        print(progress_tracker.generate_report())
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")
