import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('titanic.csv')

df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Fare']].values
y = df['Survived'].values


lr = LogisticRegression()
lr.fit(X, y) # Verilen eğitim verilerine göre model oluşturulması

print(lr.predict(X[:10])) # X'lerden y tahmin değerleri (ilk 10 satır)
print(y[:10]) # Gerçek değerler (ilk 10 satır)

y_tahmin = lr.predict(X) # X'lerden y tahmin değerleri

# Doğru tahmin edilen örneklerin toplam örnek sayısına bölümü: 
print("Doğruluk (Accuracy) :", (y == y_tahmin).sum() / y.shape[0]) 

# Doğruluk için score metotu ile kullanılabilir. 
print("Doğruluk (Accuracy) :", lr.score(X,y))