import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat 


"""
根据每个点拓展的近邻个数，统计每个近邻个数对应的点数，并画成柱状图。
其中柱状图的bar颜色随着高度变化而变化，使用的是summer色系。
"""

data = loadmat("./Isoface-k=5.mat")['neig'] # 1 x 698
max_neighbors = np.max(data)
min_neighbors = np.min(data)

neighbors_hist = [] # 纵坐标，统计每种近邻个数对应的点数
for i in range(max_neighbors - min_neighbors + 1):
    neighbors_hist.append(np.sum(data == min_neighbors + i))
# print(neighbors_hist)

neighbors_num = [min_neighbors + i for i in range(max_neighbors - min_neighbors + 1)] # 横坐标，所有的近邻个数
data_num = neighbors_hist

x = np.arange(len(neighbors_num))  # the label locations
width = 0.6  # the width of the bars

fig, ax = plt.subplots()
array_hist = np.array(data_num)
array_hist = (array_hist - np.min(array_hist)) / (np.max(array_hist) - np.min(array_hist))
colors = plt.cm.summer(1 - array_hist)
rects2 = ax.bar(x, data_num, width, color=colors)

ax.set_xlabel(r'$\|N_i \cup$$(\cup_{l=1}^{k} N_{il})\|$')
ax.set_ylabel(r'The number of each $\|N_i \cup$$(\cup_{l=1}^{k} N_{il})\|$') # in Statue-Face dataset
ax.set_xticks(x)
ax.set_xticklabels(neighbors_num)
plt.ylim(0, max(neighbors_hist) + 50)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects2)
fig.tight_layout()
plt.show()