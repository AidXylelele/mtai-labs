import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

membership = fuzz.zmf(x, 3, 6)

fig, ax = plt.subplots()

ax.plot(x, membership, 'r', linewidth=1.5, label='Z-shaped Membership Function')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Z-shaped Membership Function')

ax.legend()

plt.grid()
plt.show()
