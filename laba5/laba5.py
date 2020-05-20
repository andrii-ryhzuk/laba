import pandas as pd

df = pd.read_csv('500_Cities__City-level_Data__GIS_Friendly_Format___2019_release.csv', sep=',', index_col=0)


print('Corr by Pearson')
pears = df.corr(method='pearson')
print(pears)


print('Corr by Spearman')
spear = df.corr(method='spearman')
print(spear)