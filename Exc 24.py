# checking age for a credit card request
age = int(input("Enter your age: "))
eligible = "Eligible for a credit card."
not_eligible = "You do not meet the requirements."

if age >= 18 and age < 80:
    print(eligible)
elif age > 80:
    health_cert_num = input("Enter your health certificate number: ")

    try:
        health_cert_num = int(health_cert_num)
        if 0 < health_cert_num <= 10:
            print(eligible)
        else:
            print(not_eligible)
    except ValueError:
        print("Invalid health certificate number. Please enter a valid number.")

else:
    print(not_eligible)
