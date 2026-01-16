import tkinter as tk
from tkinter import messagebox
import random

class MayinTarlasiGUI:
    def __init__(self, pencere, olcek=10):
        self.pencere = pencere
        self.pencere.title("Mayın Tarlası")
        self.olcek = olcek
        self.butonlar = [[None for _ in range(olcek)] for _ in range(olcek)]
        self.tarla = [[0] * olcek for _ in range(olcek)]
        self.toplam_mayin = 0
        
        self.oyunu_kur()
        self.arayuzu_olustur()

    def oyunu_kur(self):
        # Mantık: Mayınları yerleştir ve sayıları hesapla
        for i in range(self.olcek):
            for j in range(self.olcek):
                if random.random() < 0.15: # %15 mayın ihtimali
                    self.tarla[i][j] = '*'
                    self.toplam_mayin += 1
                    # Çevredeki sayıları artır
                    for di in (-1, 0, 1):
                        for dj in (-1, 0, 1):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.olcek and 0 <= nj < self.olcek:
                                if isinstance(self.tarla[ni][nj], int):
                                    self.tarla[ni][nj] += 1

    def arayuzu_olustur(self):
        # Grid (ızgara) yapısıyla butonları oluşturma
        for r in range(self.olcek):
            for c in range(self.olcek):
                btn = tk.Button(self.pencere, text=" ", width=4, height=2, 
                               command=lambda r=r, c=c: self.hucre_tikla(r, c),
                               font=('Arial', 10, 'bold'), bg="#CCCCCC")
                btn.grid(row=r, column=c)
                self.butonlar[r][c] = btn

    def hucre_tikla(self, r, c):
        # Eğer hücre zaten açılmışsa işlem yapma
        if self.butonlar[r][c]["state"] == "disabled":
            return

        icerik = self.tarla[r][c]

        if icerik == '*':
            self.butonlar[r][c].config(text="💣", bg="red")
            self.oyun_bitti(False)
        else:
            self.hucre_ac(r, c)
            if self.kazanma_kontrol():
                self.oyun_bitti(True)

    def hucre_ac(self, r, c):
        # Senin 'tarla_acici' fonksiyonunun GUI versiyonu
        if self.butonlar[r][c]["state"] == "disabled":
            return

        deger = self.tarla[r][c]
        self.butonlar[r][c].config(text=deger if deger > 0 else "", 
                                   state="disabled", relief=tk.SUNKEN, bg="#EEEEEE")

        # Eğer hücre 0 ise komşuları da aç (Rekürsif)
        if deger == 0:
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = r + di, c + dj
                    if 0 <= ni < self.olcek and 0 <= nj < self.olcek:
                        self.hucre_ac(ni, nj)

    def kazanma_kontrol(self):
        # Kapalı olan ve mayın olmayan hücre var mı?
        for r in range(self.olcek):
            for c in range(self.olcek):
                if self.tarla[r][c] != '*' and self.butonlar[r][c]["state"] != "disabled":
                    return False
        return True

    def oyun_bitti(self, kazandi):
        # Tüm mayınları göster
        for r in range(self.olcek):
            for c in range(self.olcek):
                if self.tarla[r][c] == '*':
                    self.butonlar[r][c].config(text="💣", bg="#FFAAAA")
                self.butonlar[r][c].config(state="disabled")

        mesaj = "Tebrikler, Kazandınız!" if kazandi else "Mayına Bastınız! Oyun Bitti."
        messagebox.showinfo("Sonuç", mesaj)
        self.pencere.destroy()

# Uygulamayı başlat
root = tk.Tk()
uygulama = MayinTarlasiGUI(root, olcek=10)
root.mainloop()
