# fizzbuzz exemple 2 in a sinle line
def fizz_buzz(input):
    return "FizzBuzz" if input % 15 == 0 else "Fizz" if input % 3 == 0 else "Buzz" if input % 5 == 0 else input
