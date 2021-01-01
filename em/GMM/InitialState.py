import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import random

m1 = [1, 1]
m2 = [7, 7]
cov1 = [[3, 2], [2, 3]]
cov2 = [[2, -1], [-1, 2]]
x = np.random.multivariate_normal(m1, cov1, size=(200,))
y = np.random.multivariate_normal(m2, cov2, size=(200,))
d = np.concatenate((x, y), axis=0)

m1 = random.choice(d)
m2 = random.choice(d)
cov1 = np.cov(np.transpose(d))
cov2 = np.cov(np.transpose(d))
pi = 0.4
x1 = np.linspace(-4, 11, 200)
x2 = np.linspace(-4, 11, 200)
X, Y = np.meshgrid(x1, x2)
Z1 = multivariate_normal(m1, cov1)
Z2 = multivariate_normal(m2, cov2)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

plt.figure(figsize=(10, 10))
plt.scatter(d[:, 0], d[:, 1], marker='o')
plt.contour(X, Y, Z1.pdf(pos), colors="r", alpha=0.5)
plt.contour(X, Y, Z2.pdf(pos), colors="b", alpha=0.5)
plt.axis('equal')
plt.xlabel('X-Axis', fontsize=16)
plt.ylabel('Y-Axis', fontsize=16)
plt.title('Initial State', fontsize=22)
plt.grid()
plt.show()
