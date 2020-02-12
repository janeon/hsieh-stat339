import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import minmax_scale

f = open("big_matrix.txt", "r")
A = np.loadtxt(f)
R = np.size(A, 0)
C = np.size(A, 1)

# print(A[0][0], A[-1][-1])
epsilon = 0.01
A_scaled = minmax_scale(A, feature_range=(epsilon,1-epsilon))


# print(A_scaled[0][0], A_scaled[-1][-1])
plt.imshow(A_scaled, cmap="gray")
plt.show()
