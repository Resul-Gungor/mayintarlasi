import random

masa = []
satırlar = [[] * 9 for a in range(9)]
sütunlar = [[] * 9 for a in range(9)]
kareler = [[] * 3 for a in range(3)]

for i in range(9):
    for j in range(9):
        satırlar[i][j] = random.randint(1, 9)


# satırlar = [ [] [] [] [] [] [] [] [] [] ]
print(satırlar)