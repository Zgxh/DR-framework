import numpy as np
import matplotlib.pyplot as plt

'''
绘制statue-face数据集的高维重建误差曲线。
k的范围：2~20
数据集大小：n=200
'''

x = np.array([i for i in range(2, 21)]) # 横坐标
y = np.array([[4.4418,4.0819,3.7914,3.6932,3.6116,3.592,3.5746,3.5707,3.5661,3.5627,3.5592,3.5565,3.5542,3.552,3.5494,3.547,3.5449,3.5431,3.5416],
              [4.4418,4.0821,3.792,3.6957,3.6176,3.6041,3.5955,3.6017,3.6093,3.6182,3.6285,3.6405,3.6544,3.6696,3.6851,3.7013,3.7186,3.7364,3.7549],
              [0.0009,0.7698,0.0072,0.5688,0.0061,0.2318,0.0228,0.0998,0.0618,0.1011,0.086,0.1155,0.1166,0.1294,0.1424,0.1604,0.174,0.1732,0.1786],
              [0.0016,0.0085,0.0135,0.0257,0.0274,0.0414,0.0451,0.06,0.0674,0.0815,0.0929,0.1071,0.1218,0.1365,0.1512,0.1666,0.1818,0.1971,0.2127],
              [0.0186,1.5955,2.4314,2.4564,2.4308,2.1772,1.5088,1.2552,0.7728,0.5533,0.3412,0.2929,0.2706,0.2637,0.2537,0.2787,0.3003,0.327,0.3488]])

fig, ax = plt.subplots()
ax.plot(x, y[0,:], marker='.', c='grey', linestyle='-', label='LLE')
ax.plot(x, y[1,:], marker='o', c='darkturquoise', linestyle='-', label='MLLE')
ax.plot(x, y[2,:], marker='^', c='salmon', linestyle='-', label='IHNE')
ax.plot(x, y[3,:], marker='+', c='mediumslateblue', linestyle='-', label='RHNE')
ax.plot(x, y[4,:], marker='D', c='yellowgreen', linestyle='-', label='BHNE')

plt.ylim(-1, 8)
ax.set_ylabel('Average R. E.')
ax.set_xlabel('Neighborhood size')
plt.legend(loc='uper right')

plt.show()