import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat 


"""
根据每个点拓展的近邻个数，统计每个近邻个数对应的点数，并画成柱状图。
其中柱状图的bar颜色随着高度变化而变化，使用的是summer色系。
"""

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


data1 = loadmat("./Isoface-k=5.mat")['neig'] # 1 x 698
data2 = loadmat("./Isoface-zhexian.mat")['pltg'][2, :] # 1 x 16

max_neighbors = np.max(data1)
min_neighbors = np.min(data1)

neighbors_hist = [] # 纵坐标，统计每种近邻个数对应的点数
for i in range(max_neighbors - min_neighbors + 1):
    neighbors_hist.append(np.sum(data1 == min_neighbors + i))
# print(neighbors_hist)

neighbors_num = [min_neighbors + i for i in range(max_neighbors - min_neighbors + 1)] # 横坐标，所有的近邻个数
data1_num = neighbors_hist

x = np.arange(len(neighbors_num))  # the label locations
width = 0.6  # the width of the bars

# calculate color bar of hist
array_hist = np.array(data1_num)
array_hist = (array_hist - np.min(array_hist)) / (np.max(array_hist) - np.min(array_hist))
colors = plt.cm.summer(1 - array_hist)

fig, ax = plt.subplots()
# hist
rects1 = ax.bar(x, data1_num, width, color=colors, label='The number of each $P$')
# autolabel(rects1) # 显示数值
# ax.set_xlabel(r'$\|N_i \cup$$(\cup_{l=1}^{k} N_{il})\|$')
ax.set_xlabel('$P$')
ax.set_ylabel('The number of each $P$') # in Statue-Face data1set
ax.set_xticks(x)
ax.set_xticklabels(neighbors_num)
ax.set_ylim(0, max(neighbors_hist) + 50)
ax.legend(prop={'size':8},loc=1)

# line graph
ax2 = ax.twinx()
rects2 = ax2.plot(x, data2, c='k', marker='.', label='The frequency of $x_i$')
ax2.set_ylim(0, max(data2) + 100)
ax2.set_ylabel("The frequency of $x_i$")
ax2.legend(prop={'size':8},loc=2)
# plt.legend(prop={'family':'SimHei','size':8},loc="upper left") 
# for i, (_x, _y) in enumerate(zip(x, data2)):  
#     plt.text(_x, _y, data2[i], color='black', fontsize=10,)  # 将数值显示在图形上


fig.tight_layout()
plt.show()