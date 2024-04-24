import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([9,1,0,2,5])
y = np.array([1,4,3,5,0])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([10, 12, 20, 31])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()