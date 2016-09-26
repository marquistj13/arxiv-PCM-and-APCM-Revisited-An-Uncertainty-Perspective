# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

def f(u):
    return u*np.log(u)-u #the cost function of membership
    # return np.log(u)# its derivative
v_f=np.vectorize(f)

x=np.r_[0.01:1:100j]
fig,ax=plt.subplots()
ax.plot(x,map(v_f,x),'.', color=colors[0])
plt.show()
