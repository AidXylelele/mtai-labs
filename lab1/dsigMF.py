import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(-5, 15, 100)

dsig_membership = fuzz.dsigmf(x, 3, 5, 6, 8)

fig, ax = plt.subplots()

ax.plot(x, dsig_membership, 'r', linewidth=1.5, label='Symmetric Sigmoid')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Symmetric Sigmoid Membership Function')

ax.legend()

plt.grid()
plt.show()
