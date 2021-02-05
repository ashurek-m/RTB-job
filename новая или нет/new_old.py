import pandas as pd
import time, csv

def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)
        csv_file.close()

start_time = time.time()
dl_obr = pd.read_excel('длина_обработки.xls', header=0)
proizv = pd.read_excel('ПРОИЗВ_АРХИВ ПРОИЗВ.xls', header=0)

# str_numder_order = proizv.loc[:, ['НомерЗаказа']]
# numder_order = []
# for j in range(len(str_numder_order)):
    # ch = float(str_numder_order[j])
    # numder_order.append(ch)
# proizv1 = proizv.assing(numder_order=int(proizv['НомерЗаказа']))

good_numder_order = proizv[proizv['НомерЗаказа'] < 40000]
ref_baan = good_numder_order['КодBAAN'].unique()
ref_oreder = []
for i in range(len(ref_baan)):
    items = dl_obr[dl_obr['код'] == ref_baan[i]].reset_index(drop=True)
    items2 = items.loc[:, 'дата передачи БМР']
    items3 = items.loc[:, 'item']
    for j in range(len(items2)):
        date = items2[j]
        list1 = []
        count_orders1 = proizv[proizv['КодBAAN'] == ref_baan[i]]
        count_orders2 = count_orders1[count_orders1['ДатаДобавленияЗаписи'] <= date]
        count_orders3 = len(count_orders2['НомерЗаказа'].unique())
        list1.append(items3[j])
        list1.append(ref_baan[i])
        list1.append(count_orders3)
        if count_orders3 > 1:
            list1.append(200000)
        else:
            list1.append(100000)
        ref_oreder.append(list1)


df = pd.DataFrame(ref_oreder, columns=['item', 'cod', 'count', 'XXXXXX'])
writer = pd.ExcelWriter('new_old.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()
print(ref_oreder[20])
print("--- %s seconds ---" % (time.time() - start_time))


