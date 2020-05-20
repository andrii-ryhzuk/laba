import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pylab import *
from scipy.linalg import *

# читаем данные из файлов
x = np.array([-1, -1, 0, 1, 2,3])
y = np.array([-1, 0, 1, 1, 3, 5])

# задаем вектор m = [x**2, x, E]
m = vstack((x ** 2, x, ones(6))).T
# находим коэффициенты при составляющих вектора m
s = lstsq(m, y)[0]
# на отрезке [-5,5]
x_prec = linspace(-5, 5, 101)
# рисуем теоретическую кривую
plot(x_prec, x_prec ** 2, '--', lw=2)
# рисуем точки
plot(x, y, 'D')
plot(x_prec, s[0] * x_prec ** 2 + s[1] * x_prec + s[2], '-', lw=2)
grid()
plt.show()
plt.savefig('plot_lab_6.png')


df = pd.read_csv('Advertising.csv', sep=',', index_col='id')
sns.pairplot(df)
plt.show()

fig, axs = plt.subplots(1, 3, sharey=True)
df.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16, 8))
df.plot(kind='scatter', x='radio', y='sales', color='red', ax=axs[1])
df.plot(kind='scatter', x='newspaper', y='sales', color='green', ax=axs[2])
plt.show()

import statsmodels.formula.api as smf
lm = smf.ols(formula='sales~TV', data=df).fit()
print(lm.params)

X_new = pd.DataFrame({'TV': [50]})
print(X_new.head())
print(lm.predict(X_new))
