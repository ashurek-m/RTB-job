from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import pandas as pd


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


df = pd.read_excel('C:\\Users\\oshurek_m\\Desktop\\Пеленг общий.xlsx', sheet_name='matmod')
df_1 = df[['Индекс RTB', 'Наименование детали', 'Кол-во', 'N° ITEM', 'Стоимость, $', 'CN', 'DART', 'TOUR']]
df_2 = df_1.dropna(axis=0)
df_2.info()
# величина смены в часах
b = 8 * 0.8
# кол-во смен в месяце
c = 42
model = LpProblem('prod', LpMaximize)
names_det = list(df_2['N° ITEM'])
print(len(names_det))
costs = dict(zip(names_det, df_2['Стоимость, $']))
cn = dict(zip(names_det, df_2['CN']))
dart = dict(zip(names_det, df_2['DART']))
tour = dict(zip(names_det, df_2['TOUR']))

vat = LpVariable.dicts('vat', names_det, cat='Binary')

costs_1 = []
for n in vat:
    costs_1.append(n)
print(costs_1)
cost_s1 = pd.Series(data=costs_1, name='N° ITEM')
cost_df = cost_s1.to_frame()
cost_df.info()
cost_2 = []
for k in vat:
    cost_2.append(vat[k])
cost_df = cost_df.assign(re_name=cost_2)

model += lpSum(costs[i]*vat[i] for i in names_det)
t_cn = 350
t_dart = 20
t_tour = 100
model += lpSum(cn[i]*vat[i] for i in names_det) <= 350
model += lpSum(dart[i]*vat[i] for i in names_det) <= 20
model += lpSum(tour[i]*vat[i] for i in names_det) <= 100
for i in names_det:
    model += (cn[i]*vat[i]) <= c * b
    model += (dart[i]*vat[i]) <= c * b
    model += (tour[i]*vat[i]) <= c * b
model.solve()
var_list = []
print("Status:", LpStatus[model.status])

for v in model.variables():
    var_list_2 = [v.name, v.varValue]
    var_list.append(var_list_2)

df_var = pd.DataFrame(data=var_list, columns=['re_name', 'var'])
print(df_var.head())
print(cost_df.head())
df = df_var.merge(cost_df, on='re_name', how='outer')

save_excel('C:\\Users\\oshurek_m\\Desktop\\matmod.xlsx', df)

'''https://proglib.io/p/lineynoe-programmirovanie-praktika-resheniya-zadach-optimizacii-na-python-2020-11-26 
https://www.machinelearningmastery.ru/linear-programming-and-discrete-optimization-with-python-using-pulp
-449f3c5f6e99/ '''