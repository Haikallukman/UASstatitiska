import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


mean = [0, 0, 0]
cov = [
    [1.0, 0.8, 0.6],
    [0.8, 1.0, 0.7],
    [0.6, 0.7, 1.0]
]



data = np.random.multivariate_normal(mean, cov, 1000)


X = data[:, 0]
Y = data[:, 1]
Z = data[:, 2]


corr_matrix = np.corrcoef(data.T)
print("Matriks Korelasi:")
print(corr_matrix)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, s=30, alpha=0.6)


ax.set_title("Variabel Random Multivariat (3 Dimensi)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()


plt.figure(figsize=(6, 5))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    xticklabels=["X", "Y", "Z"],
    yticklabels=["X", "Y", "Z"]
)
plt.title("Heatmap Korelasi Antar Variabel")
plt.show()
