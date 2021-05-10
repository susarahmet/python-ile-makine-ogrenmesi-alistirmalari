import pandas as pd
df = pd.read_csv('titanic.csv')

import matplotlib.pyplot as plt

# Veri çizimi için scatter:
plt.scatter(df['Age'], df['Sex'], c=df['Survived'])
plt.show()

plt.plot([0, 100], [0, 50])
plt.show()

plt.scatter(df['PassengerId'], df['Age'])
plt.plot([0, 800], [20, 60])
plt.show()

