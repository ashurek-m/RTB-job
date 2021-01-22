import pandas as pd
import xlrd
csv = pd.read_csv(r"C:\Python's_project\RTB-job\address_file.csv", names=['path'])
clean_address = csv.loc[:, 'path']
sum1 = 0
sum2 = 0
sum3 = 0
error_list = []
for i in range(len(clean_address)):
    try:
        way = str(clean_address[i])
        df = pd.read_excel(way, sheet_name='расчет')
        sum1 += 1
    except xlrd.biffh.XLRDError:
        error_list.append(clean_address[i])
        sum2 += 1
        continue
    except PermissionError:
        error_list.append(clean_address[i])
        sum3 += 1
        continue


print(len(clean_address))
print(f'открылось файлов {sum1}')
print(f'не открылось файлов из-за отсуствия листа расчет {sum2}')
print(f'не открылось по другой причине {sum3}')