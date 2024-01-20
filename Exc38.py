sorular = (
    "1. Güneş sistemindeki en büyük gezegen hangisidir?:",
    "2. Hangi gök cismi dünyaya daha yakındır?:",
    "3. Güneş sistemimizin merkezindeki yıldızın adı nedir?:",
    "4. Hangi gezegen 'kızıl gezegen' olarak bilinir?:",
    "5. Dünyanın doğal uydusunun adı nedir?:",
)
cevaplar = ("B", "D", "C", "C", "B")
seçenekler = (
    ("A. Dünya", "B. Jüpiter", "C. Mars", "D. Venüs"),
    ("A. Mars", "B. Venüs", "C. Jüpiter", "D. Ay"),
    ("A. Ay", "B. Venüs", "C. Güneş", "D. Mars"),
    ("A. Jüpiter", "B. Satürn", "C. Mars", "D. Neptün"),
    ("A. Mars", "B. Ay", "C. Satürn", "D. Merkür"),
)
tahminler = []
puan = 0
soru_no = 0

for soru in sorular:
    print("----------------------")
    print(soru)
    for seçenek in seçenekler[soru_no]:
        print(seçenekler)

    tahmin = input("Şık seçin (A, B, C, D): ").upper()
    tahminler.append(tahmin)
    if tahmin == cevaplar[soru_no]:
        puan += 1
        print("Doğru Cevap!")
    else:
        print("Hatalı Yanıt!")
        print(f"{cevaplar[soru_no]} doğru yanıt olacak.")
    soru_no += 1

print("----------------------")
print("       SONUÇ        ")
print("----------------------")

print("cevaplar: ", end="")
for Cevap in cevaplar:
    print(Cevap, end=" ")
print()

print("tahm'nler: ", end="")
for tahmin in tahminler:
    print(tahmin, end=" ")
print()

puan = int(puan / len(cevaplar) * 100)
print(f"Toplam puanın: {puan}%")
