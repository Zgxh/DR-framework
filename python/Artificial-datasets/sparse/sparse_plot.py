import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D 
from scipy.io import loadmat 


def plot(data, labels):

	"""Plot distribution of high-dimensonal data."""

	c = (labels[:, 0] - np.min(labels[:, 0])) / (np.max(labels[:, 0]) - np.min(labels[:, 0]))
	fig = plt.figure(figsize=(4, 4))
	ax = Axes3D(fig)
	ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=c, cmap='plasma', marker='.')
	ax.axis('off')
	# ax.grid(False)
	# ax.set_xticks([])
	# ax.set_yticks([])
	# ax.set_zticks([])
	# ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	# ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	# ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
	plt.show()


def plot_Y(Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y21, Y22, Y23, Y24, Y25, Y26, Y27, Y28, labels):

	"""Plot distribution of low-dimensional data."""

	c = (labels[:, 0] - np.min(labels[:, 0])) / (np.max(labels[:, 0]) - np.min(labels[:, 0]))
	plt.figure(figsize=(15, 4))

	ax1 = plt.subplot(281)
	plt.scatter(Y11[:, 0], Y11[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax1.set_title('A', fontsize=15, fontweight='medium', loc='center')

	ax2 = plt.subplot(282)
	plt.scatter(Y12[:, 0], Y12[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax2.set_title('B', fontsize=15, fontweight='medium', loc='center')
	
	ax3 = plt.subplot(283)
	plt.scatter(Y13[:, 0], Y13[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax3.set_title('C', fontsize=15, fontweight='medium', loc='center')

	ax4 = plt.subplot(284)
	plt.scatter(Y14[:, 0], Y14[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax4.set_title('D', fontsize=15, fontweight='medium', loc='center')
	
	ax5 = plt.subplot(285)
	plt.scatter(Y15[:, 0], Y15[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax5.set_title('E', fontsize=15, fontweight='medium', loc='center')

	ax6 = plt.subplot(286)
	plt.scatter(Y16[:, 0], Y16[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax6.set_title('F', fontsize=15, fontweight='medium', loc='center')

	ax7 = plt.subplot(287)
	plt.scatter(Y17[:, 0], Y17[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax7.set_title('G', fontsize=15, fontweight='medium', loc='center')

	ax8 = plt.subplot(288)
	plt.scatter(Y18[:, 0], Y18[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	# ax8.set_title('H', fontsize=15, fontweight='medium', loc='center')

	ax9 = plt.subplot(289)
	plt.scatter(Y21[:, 0], Y21[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax9.set_title('A', fontsize=15, fontweight='medium', loc='center')

	ax10 = plt.subplot(2,8,10)
	plt.scatter(Y22[:, 0], Y22[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax10.set_title('B', fontsize=15, fontweight='medium', loc='center')
	
	ax11 = plt.subplot(2,8,11)
	plt.scatter(Y23[:, 0], Y23[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax11.set_title('C', fontsize=15, fontweight='medium', loc='center')

	ax12 = plt.subplot(2,8,12)
	plt.scatter(Y24[:, 0], Y24[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax12.set_title('D', fontsize=15, fontweight='medium', loc='center')
	
	ax13 = plt.subplot(2,8,13)
	plt.scatter(Y25[:, 0], Y25[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax13.set_title('E', fontsize=15, fontweight='medium', loc='center')

	ax14 = plt.subplot(2,8,14)
	plt.scatter(Y26[:, 0], Y26[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax14.set_title('F', fontsize=15, fontweight='medium', loc='center')

	ax15 = plt.subplot(2,8,15)
	plt.scatter(Y27[:, 0], Y27[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax15.set_title('G', fontsize=15, fontweight='medium', loc='center')

	ax16 = plt.subplot(2,8,16)
	plt.scatter(Y28[:, 0], Y28[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	ax16.set_title('H', fontsize=15, fontweight='medium', loc='center')

	plt.show()


def main():

	p = 15
	k1 = 7
	k2 = 11


	data = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\X_p={0}.mat".format(p))['X']
	labels = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\labels_p={0}.mat".format(p))['labels']

	Y11 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_LLE_k={1}.mat".format(p, k1))['mappedX']
	Y12 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_HLLE_k={1}.mat".format(p, k1))['mappedX']
	Y13 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_LLC_k={1}.mat".format(p, k1))['mappedX']
	Y14 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_LTSA_k={1}.mat".format(p, k1))['mappedX']
	Y15 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_MLLE_k={1}.mat".format(p, k1))['mappedX']
	Y16 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_IHNE_k={1}.mat".format(p, k1))['mappedX']
	Y17 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_RHNE_k={1}.mat".format(p, k1))['mappedX']
	Y18 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_BHNE_k={1}.mat".format(p, k1))['mappedX']

	Y21 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_LLE_k={1}.mat".format(p, k2))['mappedX']
	Y22 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_HLLE_k={1}.mat".format(p, k2))['mappedX']
	Y23 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_LLC_k={1}.mat".format(p, k2))['mappedX']
	Y24 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_LTSA_k={1}.mat".format(p, k2))['mappedX']
	Y25 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_MLLE_k={1}.mat".format(p, k2))['mappedX']
	Y26 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_IHNE_k={1}.mat".format(p, k2))['mappedX']
	Y27 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_RHNE_k={1}.mat".format(p, k2))['mappedX']
	Y28 = loadmat("MnifoldLearning\experiments\Artificial-datasets\sparse\p={0}\Y_p={0}_BHNE_k={1}.mat".format(p, k2))['mappedX']

	# plot(data, labels)
	plot_Y(Y11, Y12, Y13, Y14, Y15, Y16, Y17, Y18, Y21, Y22, Y23, Y24, Y25, Y26, Y27, Y28, labels)

	
if __name__ == "__main__":
	main()