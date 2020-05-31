import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D 
from scipy.io import loadmat 



def plot(data, label):

	"""Plot distribution of high-dimensonal data."""

	c = (label[:, 0] - np.min(label[:, 0])) / (np.max(label[:, 0]) - np.min(label[:, 0]))
	fig = plt.figure(figsize=(4, 4))
	ax = Axes3D(fig)
	ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=c, cmap='plasma', marker='.')
	ax.axis('off')
	plt.show()


def plot_Y(Y1, Y2, label1, label2):

	"""Plot distribution of low-dimensional data."""

	c1 = (label1[:, 0] - np.min(label1[:, 0])) / (np.max(label1[:, 0]) - np.min(label1[:, 0]))
	c2 = (label2[:, 0] - np.min(label2[:, 0])) / (np.max(label2[:, 0]) - np.min(label2[:, 0]))
	plt.figure(figsize=(4, 4))
	plt.subplot(211)
	plt.scatter(Y1[:, 0], Y1[:, 1], c=c1, cmap='plasma', marker='.')
	plt.axis('off')
	plt.subplot(212)
	plt.scatter(Y2[:, 0], Y2[:, 1], c=c2, cmap='plasma', marker='.')
	plt.axis('off')
	plt.show()


def main():
	# data1 = loadmat("MnifoldLearning\experiments\Artificial-datasets\ex1\data_swiss.mat")['X']
	# data2 = loadmat("MnifoldLearning\experiments\Artificial-datasets\ex1\data_swiss-hole.mat")['X']
	label1 = loadmat("MnifoldLearning\experiments\Artificial-datasets\ex1\label_swiss.mat")['labels']
	label2 = loadmat("MnifoldLearning\experiments\Artificial-datasets\ex1\label_swiss-hole.mat")['labels']
	Y1 = loadmat("MnifoldLearning\experiments\Artificial-datasets\ex1\dirAML_swiss.mat")['Y']
	Y2 = loadmat("MnifoldLearning\experiments\Artificial-datasets\ex1\dirAML_hole.mat")['Y']
	plot_Y(Y1, Y2, label1, label2)
	# plot(data2, label2)
	

if __name__ == "__main__":
	main()