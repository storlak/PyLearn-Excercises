# calculate the future value of 1000USD with %3 interest rate, 5 years investment time.
amount = 1000
rate = 0.03
time = 5
future_value = amount * pow(1 + rate, time)
print(f"Future value: ${future_value:.2f}")

# or

future_value = amount * (1 + rate) ** time
print(f"Future value: ${future_value:.2f}")
