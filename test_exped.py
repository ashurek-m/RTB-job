import pandas as pd

df = pd.read_excel('EXPED.xlsb', header=4, usecols='B:AC', engine='pyxlsb', skiprows=[5],nrows=2295)
print(df.head(10))
print(df.tail())
df.info()
