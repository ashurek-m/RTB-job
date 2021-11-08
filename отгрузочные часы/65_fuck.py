import step_1 as s1
import step_2 as s2
import step_3 as s3
import step_4 as s4
import pandas as pd


df = pd.read_csv('shape_65.csv')
print(df.shape)
s3.shape_r62([65], ['shape_65.csv'])