import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)

plt.plot(x, x, label="x")
plt.plot(x, 20 * x - 90, label="20x - 90")
plt.plot(x, -10 * x + 50, label="-10x + 50")
plt.plot(x, -26 * x + 125, label="-26x + 125")
plt.legend()
plt.show()
