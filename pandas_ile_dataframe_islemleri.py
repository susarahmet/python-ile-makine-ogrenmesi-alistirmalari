
import pandas as pd

df = pd.read_csv('titanic.csv')

# DataFrame'in tek sütunu Pandas Series (dizi) oluşturur. 
dizi = df['Name']
print(dizi)

# DataFrame üzerinden bir kaç sütun seçerek mini DataFrame oluşturmak mümkündür. 
# Bir sütun seçerken 1 köşeli parantez, birden çok sütun seçerken 2 köşeli parantez kullanılır. 
mini_df = df[['Name', 'Age',  'Sex', 'Survived', 'Pclass']]
print(mini_df.head())

# Yeni boolean (True or False) sütun oluşturulabilir ve DataFrame'e eklenebilir.  
mini_df['Birinci_sinif'] = df['Pclass'] == 1
print(mini_df)





