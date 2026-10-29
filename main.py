import pandas as pd
import numpy as np 
import matplotlib as mt
import matplotlib.pyplot as plt

# Первый датасет 
df = pd.read_csv('date_of_space.csv', encoding='cp1251', sep=';')
df = df.fillna(0)
df_mini = df.pivot_table(index='Country', values=['military', 'navigation', 'science', 'weather', 'all'], aggfunc='max')

df_mini = df_mini[(df_mini[['military', 'navigation', 'science', 'weather', 'all']] != 0).any(axis=1)]

# Второй датасет
df1 = pd.read_excel('da.xlsx')

df1 = df1.fillna(0)
df_min1 = df1.pivot_table(index='Country', values=['military', 'navigation', 'science', 'weather', 'all'], aggfunc='max')
df_min1 = df_min1.drop(index= 0, errors='ignore')

df_min1 = df_min1[(df_min1[['military', 'navigation', 'science', 'weather', 'all']] != 0).any(axis=1)]

# Работа с графиками matro
df_plot=df_mini[(df_mini['all']>20)].copy()
a = np.array(df_plot['all'])
b = np.array([Country[:3].upper() for Country in df_plot.index])

plt.bar(b, a, label='Запущенные спутники')
plt.plot(b, a, color='red', marker='o', markersize=7)
plt.xlabel('Страны')
plt.ylabel('Кол-во за год')
plt.title('2025')
plt.legend()
plt.show()

df_ploti=df_min1[(df_min1['all']>20)].copy()
c = np.array(df_ploti['all'])
h = np.array([Country[:3].upper() for Country in df_ploti.index])

plt.bar(h, c, label='Запущенные спутники')
plt.plot(h, c, color='red', marker='o', markersize=7)
plt.xlabel('Страны')
plt.ylabel('Кол-во за год')
plt.title('2025')
plt.legend()
plt.show()
