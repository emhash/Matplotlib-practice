import matplotlib.pyplot as plt
import numpy as np

y_data = np.array([35, 25, 25, 15])
the_labels = ["Samsang", "Redmi", "Oppo", "Huwaei"]

# if want to separate with explode.
expl = [0.1, 0, 0, 0.5]

plt.pie(y_data, labels = the_labels, explode=expl)
plt.show() 