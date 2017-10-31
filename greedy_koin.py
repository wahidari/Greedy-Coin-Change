#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 00:07:54 2017

@author: wahidari

# Algoritma Greedy Permasalahan Penukaran Uang

Diketahui:
	Jenis Koin: 1, 5, 10, 25
Ditanya:
	Jumlah Koin Minimal dengan Total Nilai Koin = 32
Jawab:
	Solusi = {25, 5, 1, 1}
    
# Kompleksitas Greedy
- Jika data tidak terurut, maka kompleksitasnya sama dengan kompleksitas algoritma pengurutannya
- Jika data terurut, maka kompleksitasnya O(n)
"""

def suitable(total, x, needle):
	return (total+x) <= needle

def greedy(C, needle):
    S = [] # Inisialisasi Himpunan Solusi
    total = 0
    while sum(S) != needle: # lakukan jika total dari solusi belum memenuhi jumlah koin
        for x in C: # telusuri himpunan kandidat (C)
            if (total+x) <= needle: # jika total + C ke-x <= needle
#                print ("total :",total,"| x :",x,"| needle :",needle)
                total += x # tambahkan x ke total
#                print ("total :",total)
                S.append(x) # tambahkan C ke-x ke himpunan solusi
    return S

if __name__ == '__main__':
    # n := Needle (Yang diinginkan)
    # C := Himpunan Kandidat
    # S := Himpunan Solusi
    n = [33000, 
         32, 
         65, 
         7]
    C = [
          [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100],
          [25, 10, 5, 1],
          [50, 25, 10, 5],
          [5, 4, 3, 1]
        ]
#    n = [32]
#    C = [[25, 10, 5, 1]]
    
#    n = [65]
#    C = [[50, 25, 10, 5]]
#
#    n = [7]
#    C = [[5, 4, 3, 1]] 
    
    for i in range(len(n)):
	    print ('\nUang Yang Ditukar:',n[i])
	    print ("Himpunan Kandidat",C[i])
	    print ('Solusi Greedy:',greedy(C[i],n[i]),"=",n[i])

