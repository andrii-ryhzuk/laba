import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt

file = pd.read_csv('2019_nCoV_data.csv', sep=';', index_col='Sno')

desc = file.describe()
print(desc)

profile = ProfileReport(file, title='Pandas Profiling Report', html={'style': {'full_width': True}})
profile.to_file(output_file="output.html")

plt.boxplot(file['Confirmed'])
plt.show()


