# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide Customized Reminder
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Modify based on time-sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the Reminder
print(reminder)
