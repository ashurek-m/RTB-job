import pandas as pd
import time


start_time = time.time()
address_file = pd.read_csv("Спектрон.csv", names=['path', 'order'])
df = address_file.loc[:, 'path']
for i in range(len(df)):
    payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
    print(payment_file.shape, address_file.loc[i, 'order'])



print("--- %s seconds ---" % (time.time() - start_time))

