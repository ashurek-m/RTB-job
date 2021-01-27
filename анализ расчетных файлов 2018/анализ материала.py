import pandas as pd
import time, csv
import xlrd

start_time = time.time()
material = pd.read_csv(r"C:\Python's_project\RTB-job\анализ расчетных файлов 2018\info_mat.csv")
locmat = pd.read_excel(r"C:\Python's_project\RTB-job\анализ расчетных файлов 2018\Копия справочник материалов LOCMAT.xls",
                       sheet_name='locmat')
print(material.duplicated(subset='наименование_материала').sum())
print(len(material['наименование_материала'].unique()))

print("--- %s seconds ---" % (time.time() - start_time))