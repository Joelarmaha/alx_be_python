# Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Initialize the reminder message
reminder = ""

# Process the Task Based on Priority
match priority:
    case "high":
        reminder = f"🔴 High Priority Task: {task}"
    case "medium":
        reminder = f"🟠 Medium Priority Task: {task}"
    case "low":
        reminder = f"🟢 Low Priority Task: {task}"
    case _:
        reminder = f"⚪ Unknown Priority Task: {task}"

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " — that requires immediate attention today!"

# Provide a Customized Reminder
print("\n Reminder:")
print(reminder)
