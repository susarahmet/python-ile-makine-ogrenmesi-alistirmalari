import numpy as np

# yaş verileri
yas_verileri = [4, 4, 7, 13, 18, 23, 24, 27, 30, 33, 55, 63, 71]

# aritmetik ortalama (mean)  
print("aritmetik ortalama", np.mean(yas_verileri))

# medyan ya da ortanca değer (median)
# eğer veri kümesi çift sayıdan oluşursa ortadaki iki sayının ortalaması alınır.
print("medyan:", np.median(yas_verileri))

# yüzdelik dilimler (percentile)
print("Yüzde 50'lik dilim: (medyan):", np.percentile(yas_verileri, 50))
print("Yüzde 25'lik dilim:", np.percentile(yas_verileri, 25))
print("Yüzde 75'lik dilim:", np.percentile(yas_verileri, 75))

# varyans değeri (variance) 
# her bir verinin ortalamaya (mean) olan uzaklıklarının karelerinin toplamının veri sayısına bölümüdür.
print("varyans:", np.var(yas_verileri))

# standart sapma (standard deviation) 
# varyans değerinin kareköküdür. 
print("standart sapma:", np.std(yas_verileri))

