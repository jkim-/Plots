import numpy as np
from scipy.interpolate import griddata
from scipy.linalg import lstsq
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

data_fname = 'surf_bias_data.txt'
data = np.genfromtxt(data_fname, skip_header=1)

X, Y = np.meshgrid(data[:,0], data[:,1])
#Z_Dtau = griddata((data[:,0], data[:,1]), data[:,2], (X, Y))#, method='cubic')
#Z_Dstau = griddata((data[:,0], data[:,1]), data[:,3], (X, Y))#, method='cubic')
#
#XX = X.flatten()
#YY = Y.flatten()

A = np.c_[data[:,0], data[:,1], np.ones(data.shape[0])]
C1,_,_,_ = lstsq(A, data[:,2])
C2,_,_,_ = lstsq(A, data[:,3])

Z1 = C1[0]*X + C1[1]*Y + C1[2]
Z2 = C2[0]*X + C2[1]*Y + C2[2]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, alpha=0.1)
ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, alpha=0.1)
#ax.scatter(data[:,0], data[:,1], data[:,2], c='r', s=50)
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
ax.axis('equal')
ax.axis('tight')
plt.show()
