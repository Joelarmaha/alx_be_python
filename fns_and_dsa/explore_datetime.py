from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    print("Current date and time:", now)
    return now

def calculate_future_date():
    number_of_days = int(input("Enter a number of days: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Date after {number_of_days} days will be:", future_date)
    return future_date