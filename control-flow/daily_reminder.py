# daily_reminder.py

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += "."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
            if time_bound == "yes":
                reminder += " Consider completing it soon."
            else:
                reminder += " You can do it when you have time."
        case "low":
            reminder = f"'{task}' is a low priority task."
            if time_bound == "yes":
                reminder += " Consider completing it when you can."
            else:
                reminder += " You can do it whenever you have free time."
        case _:
            reminder = "Invalid priority level."

    print(reminder)

if __name__ == "__main__":
    daily_reminder()
