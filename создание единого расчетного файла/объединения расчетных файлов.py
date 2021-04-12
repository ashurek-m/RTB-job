import pandas as pd
import time


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


start_time = time.time()
pay_2019 = pd.read_csv('full_pay_2019.csv')
pay_2020 = pd.read_csv('full_pay_2020.csv')
save_csv_header_w('full_pay_20019-2020.csv', pay_2019)
save_csv_header_w('full_pay_20019-2020.csv', pay_2020, w_or_a='a', columns=False)
print("--- %s seconds ---" % (time.time() - start_time))
