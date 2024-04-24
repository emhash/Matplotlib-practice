import matplotlib.pyplot as plt
import numpy as np

the_histo_random_data = np.random.normal(170, 10, 50)
# print(the_histo_random_data)
plt.hist(the_histo_random_data)
plt.show() 