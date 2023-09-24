import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)

parametrs = [2, 5, 8]

triangular_membership = fuzz.trimf(x, parametrs)

plt.figure()
plt.plot(x, triangular_membership, 'b', linewidth=1.5, label='Triangular Membership Function')
plt.title('Triangular Membership Function')
plt.xlabel('X-axis')
plt.ylabel('Membership Value')
plt.legend()
plt.grid(True)

plt.show()
