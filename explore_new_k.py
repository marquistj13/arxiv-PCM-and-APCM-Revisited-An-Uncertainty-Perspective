# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']*20
plt.style.use('ggplot')

def f(u):
    return u*np.log(u)-u #the cost function of membership
    # return np.log(u)# its derivative
v_f=np.vectorize(f)

sigma1=1
sigma2=2
def cal_eta_square(eta,sigma_v,d=1):
    return (eta+np.sqrt(eta**2+4*sigma_v*d))**2
def f_fix_eta(sigma_v,d1,d2,e1=2,e2=1.5):
    return  cal_eta_square(e1,sigma_v,d1)/cal_eta_square(e2,sigma_v,d2)
v_f_fix_eta=np.vectorize(f_fix_eta)
def f_fix_sigmav(eta1,eta2):
    sigma_v=1
    return  cal_eta_square(eta1,sigma_v)/cal_eta_square(eta2,sigma_v)
v_f_fix_sigmav=np.vectorize(f_fix_sigmav)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
d1=np.r_[0.0:10:100j]
d2=np.r_[0.0:10:100j]
D1,D2=np.meshgrid(d1,d2)
e1,e2=1.9,1.545
sigma_v=np.linspace(0.1,10,15)
Z=v_f_fix_eta(sigma_v[0],D1,D2,e1,e2)
surf = ax.plot_surface(D1, D2, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
surf = ax.plot_surface(D1, D2, e1/e2, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_xlabel('D1')
ax.set_ylabel('D2')
ax.set_zlabel('Z')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
