import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D 
from scipy.io import loadmat 
from sklearn.manifold.locally_linear import locally_linear_embedding


def plot_data(data, Y, k=5):

	"""Plot neighbors connection figure with high-dimensional data."""

	N = np.shape(data)[0]
	neighbors = find_k_neighbors(data, k)

	cmap = cm.get_cmap('plasma')
	c = (Y[:, 0] - np.min(Y[:, 0])) / (np.max(Y[:, 0]) - np.min(Y[:, 0]))
	fig = plt.figure()
	ax = Axes3D(fig)
	for i in range(N):
		for j in neighbors[i, :]:
			ax.plot([data[i, 0], data[j, 0]], [data[i, 1], data[j, 1]], [data[i, 2], data[j, 2]], linestyle='--', linewidth=1, c='silver', marker='o', markersize=7, markerfacecolor=cmap(c[i]), markeredgewidth=0)
			for m in neighbors[j, :]:
				ax.plot([data[i, 0], data[m, 0]], [data[i, 1], data[m, 1]], [data[i, 2], data[m, 2]], linestyle='--', linewidth=1, c='silver', marker='o', markersize=7, markerfacecolor=cmap(c[i]), markeredgewidth=0)

	ax.axis('off')
	plt.show()


def plot(data, Y):

	"""Plot distribution of high-dimensonal data."""

	c = (Y[:, 0] - np.min(Y[:, 0])) / (np.max(Y[:, 0]) - np.min(Y[:, 0]))
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=c, cmap='plasma', marker='.')
	ax.axis('off')
	plt.show()


def plot_Y_connect(data, Y, labels, k=5):

	"""Plot neighbors connection figure with low-dimensional data."""

	N = np.shape(data)[0]
	neighbors = find_k_neighbors(data, k)

	cmap = cm.get_cmap('plasma')
	c = (labels[:, 0] - np.min(labels[:, 0])) / (np.max(labels[:, 0]) - np.min(labels[:, 0]))
	for i in range(N):
		for j in neighbors[i, :]:
			plt.plot([Y[i, 0], Y[j, 0]], [Y[i, 1], Y[j, 1]], linestyle='--', linewidth=1, c='silver', marker='o', markersize=7, markerfacecolor=cmap(c[i]), markeredgewidth=0)
			for m in neighbors[j, :]:
				plt.plot([Y[i, 0], Y[m, 0]], [Y[i, 1], Y[m, 1]], linestyle='--', linewidth=1, c='silver', marker='o', markersize=7, markerfacecolor=cmap(c[i]), markeredgewidth=0)

	plt.axis('off')
	plt.show()


def plot_Y(Y):

	"""Plot distribution of low-dimensional data."""

	c = (Y[:, 0] - np.min(Y[:, 0])) / (np.max(Y[:, 0]) - np.min(Y[:, 0]))
	plt.scatter(Y[:, 0], Y[:, 1], c=c, cmap='plasma', marker='.')
	plt.axis('off')
	plt.show()


def find_k_neighbors(data, k=5):

	"""Find k-nearest neighbors."""

	N = np.shape(data)[0]
	distance = np.zeros((N, N), dtype=float)
	for i in range(N):
		distance[:, i] = np.sqrt(np.sum((data[i, :] - data) ** 2, axis=1))
	indices = distance.argsort(axis=1)
	neighbors = indices[:, 1:k+1]
	return neighbors


def main():
	data = loadmat("MnifoldLearning\motivation-plot\data_p=7.mat")['X']
	labels = loadmat("MnifoldLearning\motivation-plot\label_p=7.mat")['labels'] # 300, 2
	Y, err = locally_linear_embedding(data, 6, 2)
	# plot(data)
	plot_data(data, labels, k=4)
	# plot_Y(Y)
	# plot_Y_connect(data, Y, labels, k=6)


if __name__ == "__main__":
	main()