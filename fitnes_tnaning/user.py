class User:
    def __init__(self, name, age, weight, height, goal):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.workout_history = []

    def update_weight(self, new_weight):
        self.weight = new_weight

    def update_goal(self, new_goal):
        self.goal = new_goal

    def log_workout(self, workout):
        self.workout_history.append(workout)

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}cm, Goal: {self.goal}"
