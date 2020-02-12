import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.floor(x)

plt.xlabel('x axis')
plt.ylabel('y axis')
print(type(plt.step(x, y)))

plt.show()
