import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from string import ascii_letters
'''
f = open('dataset_209770_6.txt', 'r')
data = []
l = [line.strip() for line in f]
for i in range(len(l)):
    if i == 0:
        columns = l[i].split(' ')
    else:
        p = l[i].split(' ')
        data.append(p)
f.close()
df = pd.DataFrame(data=data, columns=columns)

df[['x', 'y']] = df[['x', 'y']].apply(pd.to_numeric)

sns.lmplot(x='x', y='y', data=df)


sns.set_theme(style="white")
df = pd.read_csv('genome_matrix.csv', index=True)
print(df.info())
corr = df
g = sns.heatmap(corr, cmap='viridis')
g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)


sns.set_theme(style="white")

# Generate a large random dataset
rs = np.random.RandomState(33)
d = pd.DataFrame(data=rs.normal(size=(100, 26)),
                 columns=list(ascii_letters[26:]))

# Compute the correlation matrix
corr = d.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap='viridis', vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
'''

df = pd.read_csv('dota_hero_stats.csv')
count = []
for x in df['roles']:
    count.append(len(x.split(',')))
df = df.assign(count_r=count)
df_g = df.groupby('count_r')['localized_name'].count()
print(df_g)
