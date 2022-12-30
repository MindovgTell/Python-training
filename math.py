import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('line.txt')

x = np.arange(0,100,0.1)
y = np.sin(x/10)
plt.plot(x,y)
plt.xlabel('PZDC')
plt.ylabel('hsfeuhf')

plt.legend(x,y,'auhf','dshdfdh')

plt.show()

    