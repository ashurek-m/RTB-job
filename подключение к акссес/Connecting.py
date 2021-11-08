import pyodbc

print([x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')])

'''
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    'DBQ=C:\\Users\\oshurek_m\\Desktop\\work_External_Economic.mdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)
'''