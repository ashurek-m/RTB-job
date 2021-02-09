import pandas as pd
import time


start_time = time.time()
address_file = pd.read_csv("Спектрон.csv", names=['path', 'order'])
df = address_file.loc[:, 'path']
shape_list = []
for i in range(len(df)):
    payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
    shape_list.append(payment_file.shape[1])

df_shape = pd.DataFrame(data=shape_list, columns=['кол-во_столбцов'])



print("--- %s seconds ---" % (time.time() - start_time))

