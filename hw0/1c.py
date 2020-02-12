import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(math.pi/2, step=0.01)
plt.plot(t, np.sqrt(1-t*t))
plt.plot(t, -np.sqrt(1-t*t))
plt.plot(-t, np.sqrt(1-t*t))
plt.plot(-t, -np.sqrt(1-t*t))
# plt.plot(np.cos(t), np.sin(t), linewidth=1)
plt.show()
