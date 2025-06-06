import datetime

def display_current_datetime():
    current_date = datetime.datetime(2025, 2, 4, 12, 23, 10)
    now = datetime.datetime.now()
    print("Current date and time:", now)
    return now

def calculate_future_date():
    number_of_days = int(input("Enter a number of days: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Date after {number_of_days} days will be:", future_date)
    return future_date