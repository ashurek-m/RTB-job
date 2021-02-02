import pandas as pd
import time, csv
import xlrd


def csv_writer(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


start_time = time.time()
material = pd.read_csv("info_mat.csv")
locmat = pd.read_excel("Копия справочник материалов LOCMAT.xls",
                       sheet_name='locmat')
print(material.duplicated(subset='наименование_материала').sum())
print(len(material['наименование_материала'].unique()))
# ynic = material['наименование_материала'].unique()
# path = 'уникальные_наименования_материалов.csv'
# csv_writer(spisok_spiskov(ynic), path)
unique_name_mat = material['наименование_материала'].unique()
material1 = material.replace('диаметр', '0')
unique_diameter = material1['диаметр'].unique()
print(f'уникальные диаметры {len(unique_diameter)}')
unique_name_mat_and_diameter = []
for i in range(len(unique_name_mat)):
    for j in range(len(unique_diameter)):
        unique_name_mat_and_diameter.append(
            {'name_material_payment': unique_name_mat[i],
             'estimated_size': unique_diameter[j],
             'type': 'd'}
        )

print(f'уникальный словарь типоразмеров диаметров {len(unique_name_mat_and_diameter)}')

material2 = material.replace('толщина', '0')
unique_thickness = material2['толщина'].unique()
print(f'уникальные толщины {len(unique_thickness)}')
len_ = len(unique_name_mat_and_diameter)
for i in range(len(unique_name_mat)):
    for j in range(len(unique_thickness)):
        unique_name_mat_and_diameter.append(
            {'name_material_payment': unique_name_mat[i],
             'estimated_size': unique_thickness[j],
             'type': 't'}
        )

print(f'уникальный словарь типоразмеров диаметров и толщин {len(unique_name_mat_and_diameter)}')
csv_writer(unique_name_mat_and_diameter, 'уникальные_наименования_материалов2.csv')
print("--- %s seconds ---" % (time.time() - start_time))
