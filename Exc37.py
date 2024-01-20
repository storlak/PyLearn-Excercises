questions = (
    "1. What is the largest planet in our solar system?:",
    "2. Which celestial body is closest to the Earth?",
    "3. What is the name of the star at the center of our solar system?:",
    "4. Which planet is known as the 'Red Planet'?:",
    "5. What is the name of the natural satellite that orbits the Earth?:",
)
options = (
    ("A. Earth", "B. Jupiter", "C. Mars", "D. Venus"),
    ("A. Mars", "B. Venus", "C. Jupiter", "D. Moon"),
    ("A. Moon", "B. Venus", "C. Sun", "D. Mars"),
    ("A. Jupiter", "B. Saturn", "C. Mars", "D. Neptune"),
    ("A. Mars", "B. Moon", "C. Saturn", "D. Mercury"),
)
answers = ("B", "D", "C", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
