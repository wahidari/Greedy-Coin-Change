import tkinter
from tkinter import *
import pymsgbox
root = Tk()
nilai = []
root.title("Koin Greedy")

# n := nilai yang dicari
# C := Himpunan Kandidat
# S := Himpunan Solusi
C = []

def greedy(C, nilai):
    S = [] # Inisialisasi Himpunan Solusi
    total = 0
    while sum(S) != nilai: # dilakukan jika total dari solusi kandidat memenuhi jumlah koin
        for x in C: # menelusuri himpunan kandidat (C)
            if (total+x) <= nilai: 
                # print ("total :",total,"| x :",x,"| nilai :",nilai)
                total += x # tambahkan x ke total
                # print ("total :",total)
                S.append(x) # memasukkan x kedalam himpunan solusi
    return S

def adddata():
    lendata = int(jumdata.get())
    for i in range(lendata):
        C.append(int(pymsgbox.prompt("Input koin ke. {first}: ". format(first=i+1))))
    
    #Menampilkan kandidat
    lbl_kandidat = Label(root, text="Himpunan Kandidat :")
    teks_kandidat = Label(root, text=C)
    
    #Menampilkan solusi  
    lbl_solusi = Label(root, text="Solusi Greedy :")
    cari = int(jumkoin.get())
    teks_solusi = Label(root, text=greedy(C,cari))
    
    #Menampilkan
    lbl_kandidat.grid(row=5,column=0,pady=5)
    teks_kandidat.grid(row=6,column=0,pady=5)
    lbl_solusi.grid(row=8,column=0,pady=5)
    teks_solusi.grid(row=9,column=0,pady=5)
    
#deklarasi elemen
teks_a = Label(root, text="Masukkan Jumlah data")

jumdata = Entry(root, width="20", borderwidth = 5)
jumdata.grid(row=1,column=0,columnspan=9,padx=5, pady=5,)

#Inputkan Koin yang ingin
teks_n = Label(root, text="Masukkan Koin yang ingin ditukar")
jumkoin = Entry(root, width="20", borderwidth = 5)

btn_hasil = Button(root, text="Input Nilai", bg="#B6DA8B", fg="black",   width=18, command=adddata)
btn_hasil.grid(row=4,column=0,columnspan=2, pady=20)

# mengtaur letak elemen
teks_a.grid(row=0,column=0,pady=5)
teks_n.grid(row=2,column=0,pady=5)
jumkoin.grid(row=3,column=0,columnspan=9,padx=5, pady=5,)

root.mainloop()
