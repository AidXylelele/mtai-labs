import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(-5, 15, 100)

psig_membership = fuzz.psigmf(x, 4, 5, 6, 7)

fig, ax = plt.subplots()

ax.plot(x, psig_membership, 'r', linewidth=1.5, label='Symmetric Sigmoid')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Piecewise Sigmoid Membership Function')

ax.legend()

plt.grid()
plt.show()
