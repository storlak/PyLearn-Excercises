# replace ascii with Turkish chars
def replace_ascii_with_turkish(text):
    replacements = {
        "i": "ı",
        "I": "İ",
        "g": "ğ",
        "G": "Ğ",
        "u": "ü",
        "U": "Ü",
        "o": "ö",
        "O": "Ö",
        "c": "ç",
        "C": "Ç",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


# Example usage
ascii_text = "Istanbul guzel bir sehir."
turkish_text = replace_ascii_with_turkish(ascii_text)

print(turkish_text)
