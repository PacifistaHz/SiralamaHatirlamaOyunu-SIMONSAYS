import tkinter as tk
import random
import threading


class HafizaOyunuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hafıza Oyunu")
        self.root.geometry("400x300")  # Sabit pencere boyutu
        self.root.resizable(False, False)  # Boyutlandırmayı engelle

        self.karakterler = "abcdefghıijklmnoöprsştuüvyz1234567890"
        self.soru = ""
        self.sayac = 0
        self.toplam_puan = 0

        self.create_widgets()

    def create_widgets(self):
        self.soru_label = tk.Label(self.root, text="", font=("Helvetica", 14), wraplength=350)
        self.soru_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.metin_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.metin_entry.grid(row=1, column=0, columnspan=2, pady=10)

        self.sonuc_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.sonuc_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.basla_button = tk.Button(self.root, text="Başla", command=self.basla, font=("Helvetica", 14))
        self.basla_button.grid(row=3, column=0, pady=10)

        self.devam_button = tk.Button(self.root, text="Devam Et", command=self.devam_et, font=("Helvetica", 14),
                                      state="disabled")
        self.devam_button.grid(row=3, column=1, pady=10)

        self.bitir_button = tk.Button(self.root, text="Bitir", command=self.bitir, font=("Helvetica", 14),
                                      state="disabled")
        self.bitir_button.grid(row=4, column=0, pady=10)

        self.yeniden_basla_button = tk.Button(self.root, text="Yeniden Başla", command=self.yeniden_basla,
                                              font=("Helvetica", 14))
        self.yeniden_basla_button.grid(row=4, column=1, pady=10)
        self.yeniden_basla_button.grid_remove()

    def basla(self):
        self.soru_label.config(text="Yandaki metni aklınızda tutun:")
        self.metin_entry.config(state="disabled")
        self.basla_button.config(state="disabled")
        self.devam_button.config(state="disabled")
        self.bitir_button.config(state="disabled")
        self.soru_label.after(1000, self.sonraki_soru)

    def sonraki_soru(self):
        self.karakterListesi = list(self.karakterler)
        random.shuffle(self.karakterListesi)

        self.sayac += 1
        self.soru += self.karakterListesi[self.sayac - 1] + ","
        self.soru_label.config(
            text=f"Yandaki metni aklınızda tutun: {self.soru}\n5sn süre verildi size. Bu süreyi bekleyin.")

        threading.Thread(target=self.bekle_ve_temizle).start()

    def bekle_ve_temizle(self):
        self.root.after(5000, self.temizle)

    def temizle(self):
        self.soru_label.config(text="")
        self.metin_entry.config(state="normal")
        self.metin_entry.focus()
        self.devam_button.config(state="normal")
        self.bitir_button.config(state="normal")

    def cevapla(self):
        metin = self.metin_entry.get().replace(",", "").replace(" ", "")
        soru_temiz = self.soru.replace(",", "").replace(" ", "")

        if metin == soru_temiz:
            self.sonuc_label.config(text="Tebrikler. Devam ediyor...")
            self.toplam_puan += 1
        else:
            self.sonuc_label.config(
                text=f"Oyun bitti. En fazla {self.sayac} seviyeye kadar bildiniz. Toplam puan: {self.toplam_puan}")
            self.metin_entry.config(state="disabled")
            self.devam_button.config(state="disabled")
            self.bitir_button.config(state="disabled")
            self.yeniden_basla_button.grid()

    def devam_et(self):
        self.sonuc_label.config(text="")
        self.metin_entry.delete(0, tk.END)
        self.soru_label.after(1000, self.sonraki_soru)

    def bitir(self):
        self.sonuc_label.config(
            text=f"Oyun bitti. En fazla {self.sayac} seviyeye kadar bildiniz. Toplam puan: {self.toplam_puan}")
        self.soru_label.config(text="")
        self.metin_entry.config(state="disabled")
        self.devam_button.config(state="disabled")
        self.bitir_button.config(state="disabled")
        self.yeniden_basla_button.grid()

    def yeniden_basla(self):
        self.sayac = 0
        self.soru = ""
        self.toplam_puan = 0
        self.yeniden_basla_button.grid_remove()
        self.soru_label.config(text="")
        self.metin_entry.config(state="normal")
        self.basla_button.config(state="normal")


root = tk.Tk()
app = HafizaOyunuApp(root)
root.mainloop()
