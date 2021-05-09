import pandas as pd
df = pd.read_csv('titanic.csv')

dizi = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age']].values

# Tek değer, satır ve sütun seçimleri
print(dizi[71, 3])
print(dizi[23])
print(dizi[:,1])

# Maskeleme (True/False değerler)
# Belirli kriteri sağlayan satırları seçmek için
maske=dizi[:, 1] == 1 
print(maske)        # print(dizi[:, 1] == 1) (T/F değerler)
print(dizi[maske])  # print(dizi[dizi[:, 1] == 1]) (True olan satırlar)

print(maske.sum()) # True değerlerin sayısı