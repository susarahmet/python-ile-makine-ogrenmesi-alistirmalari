import pandas as pd

# read_csv, csv uzantılı dosyayı okuyarak, DataFrame'e çevirir. 
df = pd.read_csv('titanic.csv')

# head(), DataFrame'in ilk 5 satırını (başlık dahil) döndürür.
print(df.head())

# describe(include='number'), sayısal verilerin olduğu sütunlar hakkında istatistik tablosu döndürür.
# describe(include='object'), sayısal olmayan sütunlar hakkında istatistik tablosu döndürür.
# describe(include='all'), tüm sütunlar hakkında istatistik tablosu döndürür.
# describe() karma veri kümelerinde varsayılan olarak sayısal verilerin olduğu sütunlar hakkında istatistik tablosu döndürür.
print(df.describe(include='number'))
