import numpy as np
import matplotlib.pylab as plt
x = np.linspace(-np.pi, np.pi, 5)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.show()


