import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

mean1 = 5
mean2 = 7
sigma = 1.5

membership1 = fuzz.gaussmf(x, mean1, sigma)
membership2 = fuzz.gaussmf(x, mean2, sigma)

minfunc = np.fmin(membership1, membership2)

fig, ax = plt.subplots()

ax.plot(x, membership1, 'r--', linewidth=1.5)
ax.plot(x, membership2, 'r--', linewidth=1.5)
ax.plot(x, minfunc, 'b', linewidth=1.5)

ax.set_xlabel('X-axis')
ax.set_ylabel('Membership Value')
ax.set_title('Logical and min function plot')

plt.grid()
plt.show()
