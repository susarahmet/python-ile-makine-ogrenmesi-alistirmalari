import pandas as pd

df = pd.read_csv('titanic.csv')

print(df['Age'])

# Pandas Series'i Numpy Array'e dönüştürme: 
print(df['Age'].values)


print(df[['Pclass', 'Name', 'Age']]) 

# Pandas DataFrame'i Numpy Array'e dönüştürme:
print(df[['Pclass', 'Name', 'Age']].values) 

dizi=df[['Name', 'Age', 'Fare', 'Survived']].values
# Pandas DataFrame ya da Numpy Array'in boyutu (satır, sütun):
print(dizi.shape) 




