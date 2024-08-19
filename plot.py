import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['simHei']

df = pd.read_excel('neit.xlsx')

plt.bar(df['组件'], df['数量'])
plt.xticks(rotation=75)
plt.ylim(ymin=0, ymax=10000)

for x, y in zip(df['组件'], df['数量']):
    plt.text(x, y+0.05, y, ha='center', va='bottom')

plt.show()
