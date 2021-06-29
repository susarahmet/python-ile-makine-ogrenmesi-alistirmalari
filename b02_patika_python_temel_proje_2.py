"""
Verilen listenin içindeki elemanları tersine döndüren fonksiyon: 
(Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürülür.) 

"""

liste =  [[1, 2], [3, 4], [5, 6, 7], 8, 9]
liste.reverse()

for i in range(len(liste)):
    if type(liste[i]) == list: 
        liste[i].reverse()
        
print(liste)