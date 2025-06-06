from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime(2024, 3, 25, 15, 30, 45)  # fixed current date and time
    current_date = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))
    return now

def calculate_future_date(current_date):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

current_date = display_current_datetime()
calculate_future_date(current_date)
