import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

membership_1 = fuzz.gaussmf(x, 5, 1.5)
membership_2 = fuzz.gaussmf(x, 7, 1.5)

production = membership_1 * membership_2
alg = membership_1 + membership_2 - production

fig, ax = plt.subplots()

ax.plot(x, membership_1, 'b--', linewidth=1.5)
ax.plot(x, membership_2, 'b--', linewidth=1.5)
ax.plot(x, alg, 'r', linewidth=1.5)

ax.set_xlabel('X-axis')
ax.set_ylabel('Likelihood')
ax.set_title('"AND" Operation')

ax.legend()

plt.grid()
plt.show()
