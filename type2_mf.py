# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')


def expfun(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / sigma ** 2)


def exp_marginal(x, x_mu, v0, sigma_v0):
    d = np.abs(x - x_mu)
    v_square = 0.5 * v0 ** 2 + sigma_v0 * d + 0.5 * v0 * np.sqrt(v0 ** 2 + 4 * sigma_v0 * d)
    return np.exp(-d ** 2 / v_square)


v_expfun = np.vectorize(expfun)
v_exp_marginal = np.vectorize(exp_marginal)

fig, axs = plt.subplots(1, 3, figsize=(12, 4))
# plot the primary membership function of x. sigma_x represents the bandwidth, we vary
# this parameter to see the variation of membership functio
primary_ax = axs[0]
x = np.r_[0:25:1000j]
x_mu = 12.5
sigma_x = np.r_[1:4:4j]
for i, sigma_x_i in enumerate(sigma_x):
    primary_ax.plot(x, v_expfun(x, x_mu, sigma_x_i), '.-', color=colors[i])
# plot the uncertainty of the estimated bandwidth
secondary_ax = axs[1]
v = np.r_[0:5:100j]
v0 = 2.5  # the estimated bandwidth from data
sigma_v0 = np.r_[0.1:1:4j]  # standard deviation (or uncertainty) of the bandwidth
for i, sigma_v0_i in enumerate(sigma_v0):
    secondary_ax.plot(v, v_expfun(v, v0, sigma_v0_i), '.-', color=colors[i])
# plot the marginal fuzzy set (also called membership function), we vary
# the hyper-parameter sigma_v0 to see its influence
marginal_ax = axs[2]
for i, sigma_v0_i in enumerate(sigma_v0):
    marginal_ax.plot(x, v_exp_marginal(x, x_mu, v0, sigma_v0_i), '--', color=colors[i])
for ax in axs:
    ax.set_ylim([0, 1.3])
plt.show()
