import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

mean = 5
sigma = 1.5

gaussian_membership = fuzz.gaussmf(x, mean, sigma)

fig, ax = plt.subplots()

ax.plot(x, gaussian_membership, 'r', linewidth=1.5, label='Gaussian Membership Function -- Simple')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Gaussian Membership Function -- Simple')

ax.legend()

plt.grid()
plt.show()
