import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D 
from scipy.io import loadmat 
from sklearn.manifold.locally_linear import locally_linear_embedding



def plot(data, labels):

	"""Plot distribution of high-dimensonal data."""

	c = (labels[:, 0] - np.min(labels[:, 0])) / (np.max(labels[:, 0]) - np.min(labels[:, 0]))
	fig = plt.figure(figsize=(4, 4))
	ax = Axes3D(fig)
	ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=c, cmap='plasma', marker='.')
	# ax.axis('off')
	ax.grid(False)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	plt.show()


def plot_Y(Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, labels):

	"""Plot distribution of low-dimensional data."""

	c = (labels[:, 0] - np.min(labels[:, 0])) / (np.max(labels[:, 0]) - np.min(labels[:, 0]))
	plt.figure(figsize=(12, 4))

	ax1 = plt.subplot(241)
	plt.scatter(Y1[:, 0], Y1[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax1.set_title('ORIGINAL', fontsize=15, fontweight='medium', loc='left')

	ax2 = plt.subplot(242)
	plt.scatter(Y2[:, 0], Y2[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax2.set_title('A', fontsize=15, fontweight='medium', loc='left')
	
	ax3 = plt.subplot(243)
	plt.scatter(Y3[:, 0], Y3[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax3.set_title('B', fontsize=15, fontweight='medium', loc='left')

	ax4 = plt.subplot(244)
	plt.scatter(Y4[:, 0], Y4[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax4.set_title('C', fontsize=15, fontweight='medium', loc='left')
	
	ax5 = plt.subplot(245)
	plt.scatter(Y5[:, 0], Y5[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax5.set_title('D', fontsize=15, fontweight='medium', loc='left')

	ax6 = plt.subplot(246)
	plt.scatter(Y6[:, 0], Y6[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax6.set_title('E', fontsize=15, fontweight='medium', loc='left')

	ax7 = plt.subplot(247)
	plt.scatter(Y7[:, 0], Y7[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax7.set_title('F', fontsize=15, fontweight='medium', loc='left')

	ax8 = plt.subplot(248)
	plt.scatter(Y8[:, 0], Y8[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax8.set_title('G', fontsize=15, fontweight='medium', loc='left')

	plt.show()


def main():
	data = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\data_p=15.mat")['X']
	labels = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\label_p=15.mat")['labels']
	
	Y1 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\dirAML_K=6.mat")['Y']
	Y2 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\LLE_K=6.mat")['mappedX']
	Y3 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\CLLE_K=7.mat")['mappedX']
	Y4 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\LLC_K=8.mat")['mappedX'].T
	Y5 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\LTSA_K=8.mat")['mappedX']
	Y6 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\MultiLLE_K=8.mat")['Y']
	Y7 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\dirAML_K=8.mat")['Y']
	Y8 = loadmat("MnifoldLearning\experiments\Artificial-datasets\p=15\p=15\iterAML_K=8.mat")['Y']

	# plot(data, labels)
	plot_Y(Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, labels)

	
if __name__ == "__main__":
	main()