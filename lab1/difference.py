import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

membership = fuzz.gaussmf(x, 5, 1.5)
diff_plot = 1 - membership

fig, ax = plt.subplots()

ax.plot(x, membership, 'r', linewidth=1.5)
ax.plot(x, diff_plot, 'b--', linewidth=1.5)

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Difference plot')

ax.legend()

plt.grid()
plt.show()
