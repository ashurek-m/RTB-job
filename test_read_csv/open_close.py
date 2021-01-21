import pandas as pd
import xlrd
csv = pd.read_csv(r"C:\Python's_project\RTB-job\address_file.csv", names=['path'])
clean_address = csv.loc[:, 'path']
sum1 = 0
sum2 = 0
for i in range(len(clean_address)):
    try:
        sum1 += 1
        way = str(clean_address[i])
        df = pd.read_excel(way, sheet_name='расчет')
    except xlrd.biffh.XLRDError:
        continue
    except PermissionError:
        continue

print(len(clean_address))
print(f'открылось файлов {sum1}')
print(f'не открылось файлов {sum2}')