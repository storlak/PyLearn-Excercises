from datetime import datetime

# what is my age?
while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = datetime.now().year
        age = current_year - birth_year

        if not 1910 < birth_year < current_year:
            print("Enter a valid birth year.")
        else:
            print(f"You're {age} years old.")
            break
    except ValueError:
        print("Enter a valid year.")
