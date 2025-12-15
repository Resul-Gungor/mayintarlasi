import random

olcek = int(input("Tarla ölçeğini giriniz (örn: 9 için 9x9 tarla): "))
# tarla oluşturma
tarla = [[0] * olcek for _ in range(olcek)]
toplammayin = 0
for i in range(olcek):
    for j in range(olcek):
        if random.random() < 0.20:
            tarla[i][j] = '*'
            toplammayin += 1

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < olcek and 0 <= nj < olcek:
                        if isinstance(tarla[ni][nj], int):
                            tarla[ni][nj] += 1

tarlaAciklik = [[0] * olcek for _ in range(olcek)]
def tarla_acici(a,b):
    if tarlaAciklik[a][b] == 1:
        return 1
    tarlaAciklik[a][b] = 1
    # etrafı açma
    if tarla[a][b] == 0:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni, nj = a + di, b + dj
                if 0 <= ni < olcek and 0 <= nj < olcek:
                    tarlaAciklik[ni][nj] = 1
                    if tarla[ni][nj] == 0:
                        tarla_acici(ni, nj)
                    #tarla_acici(ni, nj)

# ekran kısmı
def ekran_tarla(tarla, tarlaAciklik):
    print("      ", end='')
    for i in range(olcek):
        print('[' + chr(65 + i) + ']', end=' ')
    print()
    print("      ", end='')
    for i in range(olcek):
        print(' | ', end=' ')
    print()

    for satir in tarla:
        if tarla.index(satir) + 1 < 10:
            print(f"[ {tarla.index(satir)+1}]", end='--')
        else:
            print(f"[{tarla.index(satir)+1}]", end='--')

        for hucre in satir:
            if tarlaAciklik[tarla.index(satir)][satir.index(hucre)] == 1:
                print(f'[{hucre}]', end=' ')
            else:
                print(f'[?]', end=' ')
        print()
ekran_tarla(tarla, tarlaAciklik)
# kullanıcıdan kordinat alma kısmı
while True:
    print("\nMayınlı tarlada gezinmek için kordinat giriniz (örn: A5). Çıkmak için 'q' tuşuna basınız.")
    print(f"Toplam mayın sayısı: {toplammayin}")
    print(f"Toplam hücre sayısı: {olcek * olcek}")
    print(f"Açılan hücre sayısı: {sum(sum(1 for hucre in satir if hucre == 1) for satir in tarlaAciklik)}")
    koordinat = input("Kordinat giriniz (örn: A5): ").upper()
    if koordinat == 'Q':
        print("Oyundan çıkılıyor.")
        break
    if len(koordinat) < 2 or not koordinat[0].isalpha() or not koordinat[1:].isdigit():
        print("Geçersiz kordinat formatı. Tekrar deneyin.")
        continue

    sutun = ord(koordinat[0]) - 65
    satir = int(koordinat[1:]) - 1

    if not (0 <= sutun < olcek and 0 <= satir < olcek):
        print("Kordinatlar tarla sınırları dışında. Tekrar deneyin.")
        continue

    if tarla[satir][sutun] == '*':
        print("Mayına bastınız! Oyun bitti.")
        break
    else:
        tarla_acici(satir, sutun)
        ekran_tarla(tarla, tarlaAciklik)
        print(f"Bu hücre çevresinde {tarla[satir][sutun]} mayın var.")
        
    
