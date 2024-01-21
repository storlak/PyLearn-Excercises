questions = (
    "1. Güneş sistemindeki en büyük gezegen hangisidir?:",
    "2. Hangi gök cismi dünyaya daha yakındır?:",
    "3. Güneş sistemimizin merkezindeki yıldızın adı nedir?:",
    "4. Hangi gezegen 'kızıl gezegen' olarak bilinir?:",
    "5. Dünyanın doğal uydusunun adı nedir?:",
)
options = (
    ("A. Dünya", "B. Jüpiter", "C. Mars", "D. Venüs"),
    ("A. Mars", "B. Venüs", "C. Jüpiter", "D. Ay"),
    ("A. Ay", "B. Venüs", "C. Güneş", "D. Mars"),
    ("A. Jüpiter", "B. Satürn", "C. Mars", "D. Neptün"),
    ("A. Mars", "B. Ay", "C. Satürn", "D. Merkür"),
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

    guess = input("Şık seçin (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("DOĞRU!")
    else:
        print("YANLIŞ!")
        print(f"{answers[question_num]} doğru cevap olacak!")
    question_num += 1

print("----------------------")
print("       SONUÇLAR        ")
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
print(f"Toplam puanın: {score}%")
