import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)

gaussian_membership1 = fuzz.gauss2mf(x, 3, 1, 7, 1.5)
gaussian_membership2 = fuzz.gauss2mf(x, 3, 2, 7, 2.5)
gaussian_membership3 = fuzz.gauss2mf(x, 5, 4, 8, 3)

fig, ax = plt.subplots()

ax.plot(x, gaussian_membership1, 'r--', linewidth=1.5)
ax.plot(x, gaussian_membership2, 'g--', linewidth=1.5)
ax.plot(x, gaussian_membership3, 'b--', linewidth=1.5)

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Gaussian Membership Functions -- Complex')

ax.legend()

plt.grid()
plt.show()
