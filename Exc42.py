from datetime import timedelta, datetime

# Create a timedelta object representing 5 days, 3 hours, and 20 minutes
duration = timedelta(days=5, hours=3, minutes=20)
print(duration)  # Output: 5 days, 3:20:00

# Get the current date and time
current_datetime = datetime.now()

# Add 1 week to the current date and time
new_datetime = current_datetime + timedelta(weeks=1)
print("Today is:", current_datetime)
print("New date and time is:", new_datetime)
