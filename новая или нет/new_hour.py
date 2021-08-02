import pandas as pd


df = pd.read_excel('ПОЛНОЕ ОБЪЕД ПРОИЗВОДСТВ ТАБЛИЦ111.xlsx')
print(df.columns)

df_sdelano = df.loc[['АРХИВ_ПРОИЗВОДСТВО.N° ITEM', ]]