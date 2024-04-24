import numpy as np
import matplotlib.pyplot as plt

x_exis = np.array(["10-20","20-30","30-50","50-60","60-70","70+"])
y_exis = np.array([5,15,10,7,6,2])

plt.xlabel("Age range ")
plt.ylabel("People")
# vertical
plt.bar(x_exis,y_exis)
# horizontal
# plt.barh(x_exis,y_exis)

plt.show()