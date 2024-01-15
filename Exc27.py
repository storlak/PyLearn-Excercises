# converting Celcius and Fahrenheit
temp = float(input("Enter the temperature: "))
unit = input("Celcius(C) or Fahrenheit(F):").upper()

if unit == "C":
    temp = round(((9 * temp) / 5) + 32, 1)
    print(f"Temperature in Fahrenheit is {temp}°F.")
elif unit == "F":
    temp = round(((temp - 32) * (5 / 9)), 1)
    print(f"Temperature in Celcius is {temp}°C.")
else:
    print(f"{unit} is not a valid unit.")
