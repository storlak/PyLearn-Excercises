# listede ki en büyük sayı nasıl bulunur?
sayılar = [6, 9, 17, 29, 38, 72, 21]
enbüyük = sayılar[0]
for sayı in sayılar:
    if sayı > enbüyük:
        enbüyük = sayı
print(enbüyük)

sayılar = [6, 9, 17, 29, 38, 72, 21]
enbüyük = max(sayılar)
print(enbüyük)


