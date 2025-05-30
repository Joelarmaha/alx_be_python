# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_Bound = input("Is it time-bound? (yes/no): ")

# Initialize the reminder message
reminder = ""
match priority:
    case "high":
        reminder = f"'{task}' is a High Priority Task "
    case "medium":
        reminder = f"'{task}' is a Medium Priority Task "
    case "low":
        reminder = f"{task} is a Low Priority Task "
    case _:
        reminder = f"{task} is an Unknown Priority Task. "

# Modify reminder if the task is time-bound
if time_Bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "medium":
    reminder += " that requires immediate attention today!"
else:
    reminder += " — Consider completing it when you have free time."

# Provide a Customized Reminder
print(" Reminder:")
print(reminder)
