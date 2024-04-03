# calculating age from birth date

from datetime import datetime

# Current date and time
current_time = datetime.now()

# Birth date and time from the user with error handling
while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        birth_month = int(input("Enter your birth month (1-12): "))
        if not 1 <= birth_month <= 12:
            raise ValueError("Month must be between 1 and 12")
        birth_day = int(input("Enter your birth day (1-31): "))
        if not 1 <= birth_day <= 31:
            raise ValueError("Day must be between 1 and 31")
        birth_hour = int(input("Enter your birth hour (0-23): "))
        if not 0 <= birth_hour <= 23:
            raise ValueError("Hour must be between 0 and 23")
        birth_minute = int(input("Enter your birth minute (0-59): "))
        if not 0 <= birth_minute <= 59:
            raise ValueError("Minute must be between 0 and 59")
        break
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid value.")

# Datetime object for the birth date and time
birth_datetime = datetime(birth_year, birth_month, birth_day, birth_hour, birth_minute)

# Difference in years, months, weeks, days, and minutes
difference = current_time - birth_datetime
difference_years = difference.days // 365
difference_months = difference.days % 365 // 30
difference_days = difference.days % 365 % 30
difference_weeks = difference.days // 7
difference_minutes = difference.total_seconds() / 60

# Calculate the minutes since birth hour
minutes_since_birth_hour = difference_minutes - (birth_hour * 60 + birth_minute)

print(
    f"You have been alive for {difference_years} years, {difference_months} months, {difference_days} days, {difference_weeks} weeks, and {minutes_since_birth_hour:.2f} minutes since your birth hour."
)

# Total years, months, weeks, days, and minutes alive
total_years = difference_years
total_months = difference_years * 12 + difference_months
total_weeks = difference.days // 7
total_days = difference.days
total_minutes = difference_minutes

print(
    f"You've lived in total: "
    f"{total_years} years, "
    f"{total_months} months, "
    f"{total_weeks} weeks, "
    f"{total_days} days, "
    f"{total_minutes:.2f} minutes."
)
