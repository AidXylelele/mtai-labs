import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

smf_membership = fuzz.smf(x, 3, 7)

fig, ax = plt.subplots()

ax.plot(x, smf_membership, 'r', linewidth=1.5, label='S-Membership Function')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('S-Membership Function')

ax.legend()

plt.grid()
plt.show()
