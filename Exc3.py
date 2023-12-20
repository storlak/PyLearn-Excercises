emir = ""
mode = "kapalı"  # Default mode is "kapalı" (closed)

while True:
    emir = input("> ").lower()
    
    if emir == "çalıştır":
        if mode == "çalışıyor":
            print("Araba zaten çalışıyor.")
        else:
            print("Araba çalıştı...")
            mode = "çalışıyor"
    elif emir == "dur":
        if mode == "kapalı":
            print("Araba zaten çalışmıyor.")
        else:
            print("Araba durdu.")
            mode = "kapalı"
    elif emir == "yardım":
        print(
            """
Çalıştır: Arabayı çalıştırır.
Dur: Arabayı durdurur.
Çık: Programdan çıkar.
Yardım: Komutları gösterir."""
        )
    elif emir == "çık":
        break
    else:
        print("Hatalı emir verdiniz.")

if mode == "kapalı" and emir == "dur":
    print("Araba çalışmıyor.")
