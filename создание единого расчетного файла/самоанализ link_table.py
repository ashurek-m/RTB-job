import pandas as pd
import time

start_time = time.time()

df_link = pd.read_csv('link_table_2019-2021rev2.csv')
df_link_copy = df_link.copy()



print("--- %s seconds ---" % (time.time() - start_time))
