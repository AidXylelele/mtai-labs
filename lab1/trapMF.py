import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

parametrs = [2, 3, 7, 8]

trapezoidal_membership = fuzz.trapmf(x, parametrs)

fig, ax = plt.subplots()

ax.plot(x, trapezoidal_membership, 'b', linewidth=1.5, label='Trapezoidal Membership Function')

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Trapezoidal Membership Function')

ax.legend()

plt.grid()
plt.show()
