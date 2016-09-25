# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

def expfun(x,mu,sigma):
    return np.exp(-(x-mu)**2/sigma**2)
v_expfun=np.vectorize(expfun)
fig,axs=plt.subplots(1,3,figsize=(12,4))

primary_ax=axs[0]
x=np.r_[0:25:1000j]
x_mu=12.5
sigma_x=np.r_[1:4:4j]
for i,sigma_x_i in enumerate(sigma_x):
    primary_ax.plot(x,v_expfun(x,x_mu,sigma_x_i), '.-', color=colors[i])

secondary_ax=axs[1]
v=np.r_[0:5:100j]
v0=2.5#the bandwidth
sigma_v0=np.r_[0.1:1:4j]#standard deviation (or uncertainty) of the bandwidth

for i,sigma_v0_i in enumerate(sigma_v0):
    secondary_ax.plot(v,v_expfun(v,v0,sigma_v0_i), '.-', color=colors[i])

marginal_ax=axs[2]
def exp_marginal(x,mu,v0,sigma_v0):
    d=np.abs(x-mu)
    v_square=0.5*(v0**2+2*sigma_v0*d+2*v0*np.sqrt(v0**2+4*sigma_v0*d))
    return np.exp(-v_square/sigma_v0**2)
# def exp_marginal(x,mu,v0,sigma_v0):
#     d=np.abs(x-mu)
#     v_square=d
#     return np.exp(-v_square/sigma_v0**2)

v_exp_marginal=np.vectorize(exp_marginal)
# sigma_v0=np.r_[0.1:2:10]
# sigma_v0=[1,2.5,3]
# for i,sigma_v0_i in enumerate(sigma_v0):
# for i,sigma_v0_i in enumerate([1,2.5,3]):
#     marginal_ax.plot(x,v_exp_marginal(x,x_mu,v0,sigma_v0_i), '--', color=colors[i])
for i,v0_i in enumerate([1,2.5,3]):
    marginal_ax.plot(x,v_exp_marginal(x,x_mu,v0_i,3), '--', color=colors[i])

for ax in axs:
    ax.set_ylim([0,1.3])
plt.show()
