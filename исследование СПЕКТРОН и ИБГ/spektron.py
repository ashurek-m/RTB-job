import pandas as pd
import time, csv

start_time = time.time()
spektron_adrress_file = pd.read_csv("Спектрон.csv", names=['path'])
total = spektron_adrress_file.loc[:, 'path']
for i in range(len(total)):
    df = pd.read_excel(str(total[i]), sheet_name='расчет', header=11)


print("--- %s seconds ---" % (time.time() - start_time))
