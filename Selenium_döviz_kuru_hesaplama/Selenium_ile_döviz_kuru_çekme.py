from selenium import webdriver
from selenium.webdriver.common.by import By
import tkinter as tk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import messagebox
import time

driver = webdriver.Chrome()
driver.minimize_window()

root = tk.Tk()
root.minsize(200,200)

FONT = ("arial",20,"bold")


döviz_entry = tk.Entry(width=30)


class Döviz_incele_class():
    def __init__(self,tk_label_ = None ,tk_restart_button = None):
        self.tk_label_data = tk_label_
        self.tk_restart_button = tk_restart_button

    def Döviz_incele(self):
        if self.tk_label_data:
            self.tk_label_data.destroy()
            self.tk_restart_button.destroy()
        driver.get("https://uzmanpara.milliyet.com.tr/doviz-kurlari/")
        bekle = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[13]/div[5]/ul"))
        ).text
        dizi_data = bekle.splitlines()
        tk_button.destroy()
        WebDriverWait(driver,5)
        entry = tk.Entry(width=30)
        entry.pack()

        tk_entry_button = tk.Button(text="İncele")
        objec = Entry_incele_class(dizi_data,entry,tk_entry_button)
        tk_entry_button.config(command=objec.Entry_incele)
        tk_entry_button.pack()
        tk.Button(text="Uygulamadan Ayrıl",command=lambda :root.destroy()).pack()



class Entry_incele_class():
    def __init__(self,dizi_data,entry_data,buton_data):
        self.dizi_data = dizi_data
        self.entry = entry_data
        self.button_data = buton_data
        self.tk_label_data = None

    def Entry_incele(self):
        if self.entry.get().upper() in self.dizi_data:
            if self.tk_label_data:
                self.tk_label_data.destroy()
            index_data = self.dizi_data.index(self.entry.get().upper())
            new_data = index_data + 1
            self.tk_label_data = tk.Label(text=f"{self.dizi_data[new_data]}")
            self.tk_label_data.pack()
            self.entry.delete(0,tk.END)

        elif self.entry.get() == '' :
            messagebox.showinfo(title="BOŞ değer",message="Bir birim girin")

        else:
            tk_label = tk.Label(text="Ürün yok",font=FONT)
            tk_label.pack()
            self.button_data.destroy()
            self.entry.destroy()
            tk_restart_button = tk.Button(text="Yeniden ara")
            object_ = Döviz_incele_class(tk_label,tk_restart_button)
            tk_restart_button.config(command=object_.Döviz_incele)
            tk_restart_button.pack()
            self.tk_label_data.destroy()


obje = Döviz_incele_class()
tk_button = tk.Button(text="Taramayı Başlat",command=obje.Döviz_incele)
tk_button.pack()

root.mainloop()