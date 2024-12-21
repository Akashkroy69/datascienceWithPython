import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,5,6])
y= x*(2**2)
y1 = x*5




plt.plot(x,y1,'-')
plt.fill_between(x,y,y1,color="green",alpha=0.5)
plt.show()