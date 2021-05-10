import pandas as pd
df = pd.read_csv('titanic.csv')

#dizi = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age']].values


import matplotlib.pyplot as plt

plt.scatter(df['Age'], df['Fare'], c=df[Survived])

