import codecademylib
import numpy as np

from matplotlib import pyplot as plt

# Write matplotlib import here:

commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, bins=6, range=(20, 51))
plt.show()

