import math
def cross_entropy(p):
    return -(p*math.log(p,2)+(1-p)*math.log(1-p, 2))

# print(cross_entropy(12/17))

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5)
y = x*x+3*x+np.fabs(x)
plt.plot(x,y)
plt.show()