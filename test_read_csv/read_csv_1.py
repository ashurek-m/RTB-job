import pandas as pd

csv = pd.read_csv(r"C:\Python's_project\RTB-job\address_file.csv", names=['path'])
csv.info()
print()
print(csv.loc[0])
#df = pd.read_excel(str(csv.loc[0]), sheet_name=5,)