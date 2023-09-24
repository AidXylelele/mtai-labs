import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

gbel_membership = fuzz.gbellmf(x, 2, 5, 1)

fig, ax = plt.subplots()

ax.plot(x, gbel_membership, 'r', linewidth=1.5, label='Generalized Bell Membership Function')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Generalized Bell Membership Function')

ax.legend()

plt.grid()
plt.show()
