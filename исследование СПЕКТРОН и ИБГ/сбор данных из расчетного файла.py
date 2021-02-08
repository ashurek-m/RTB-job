import pandas as pd
import time


start_time = time.time()
address_file = pd.read_csv("Ibg.csv", names=['path'])
df = address_file.loc[:, 'path']
writer = pd.ExcelWriter('Ibg.xlsx', engine='xlsxwriter')
for i in range(len(df)):
    if i == 0:
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file.to_excel(writer, sheet_name='welcome', index=False)
        writer.save()
    else:
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file.to_excel(writer, sheet_name='welcome', index=False)

writer.save()
print("--- %s seconds ---" % (time.time() - start_time))

