import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,5,2,3,4,7])
y = np.array([9,2,1,9,3,4])

plt.title("Demo Data")
plt.xlabel("x value")
plt.ylabel("y value")

plt.plot(x, y)

plt.grid()

plt.show()