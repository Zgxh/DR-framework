import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
对teapot数据集，针对图像的重建误差，画柱状图，对应实验柱状图部分。
实验设置：n=200, k=4.
保存图像时，图像的top属性改为0.3，保存成svg图像.
"""

labels = ['Original', 'LLE', 'MLLE', 'IHNE', 'RHNE', 'BHNE'] # 横坐标
err_loc = [0, 4.0464, 4.0472, 0.0057, 0.0122, 2.8408]

x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x, err_loc, width, color='k')

ax.set_ylabel('R. E.')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.ylim(0, 10)

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