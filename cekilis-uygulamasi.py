import random as rd
import tkinter as tk

#listeler
isimler = []
hediyeler = []

#isim ekleme fonksiyonu
def isimeklesene():
    isimler.append(isimgir.get())
    isimlist.config(text=", ".join(isimler))
    isimgir.delete(0, tk.END)
    
#hediye ekleme fonksyionu
def hediyeklesene():
    hediyeler.append(hediyegir.get())
    hediyelist.config(text=", ".join(hediyeler))
    hediyegir.delete(0, tk.END)
    
#çekiliş yaptıran fonksiyon
def cekilisyap():
    rd.shuffle(isimler)
    rd.shuffle(hediyeler)

    cekilis_sonuc.config(text="")
    
    for isim, hediye in zip(isimler, hediyeler):
        cekilis_sonuc.config(text=cekilis_sonuc.cget("text") + f"{isim} --> {hediye}\n")
#sıfırla butonu
def sifirla():
    global isimler, hediyeler
    isimler = []
    hediyeler = []
    isimlist.config(text="")
    hediyelist.config(text="")
    cekilis_sonuc.config(text="")
#pencere oluşturuyoruz
pencere = tk.Tk()
pencere.title("Çekiliş Uygulaması")
pencere.geometry("300x450")

#program arayüzünün oluşturulması
isimgir_label = tk.Label(pencere, text="İsim Gir")
isimgir_label.pack()
isimgir = tk.Entry(pencere)
isimgir.pack()
ekle_buton = tk.Button(pencere, text="İsim Ekle", command=isimeklesene)
ekle_buton.pack(pady=5)

isimlerim_label = tk.Label(pencere, text="Listedeki isimler: ")
isimlerim_label.pack()
isimlist = tk.Label(pencere, text="")
isimlist.pack(pady=5)

hediyegir_label = tk.Label(pencere, text="Hediye Gir")
hediyegir_label.pack()
hediyegir = tk.Entry(pencere)
hediyegir.pack()
hedekle_buton = tk.Button(pencere, text="Hediye Ekle", command=hediyeklesene)
hedekle_buton.pack(pady=5)

hediyelerim_label = tk.Label(pencere, text="Listedeki Hediyeler: ")
hediyelerim_label.pack()
hediyelist = tk.Label(pencere, text="")
hediyelist.pack()

cekilis_buton = tk.Button(pencere, text="Çekiliş Yap", command=cekilisyap)
cekilis_buton.pack()

sifirla_buton = tk.Button(pencere, text="Sıfırla", command=sifirla)
sifirla_buton.pack(pady=10)

cekilis_sonuc = tk.Label(pencere, text="")
cekilis_sonuc.pack(padx=0)
pencere.mainloop()
