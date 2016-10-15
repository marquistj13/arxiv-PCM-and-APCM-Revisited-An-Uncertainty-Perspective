# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# the axis width also uses this value
plt.rcParams['axes.linewidth'] = 0.5

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']


# plt.style.use('ggplot')


def expfun(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / sigma ** 2)


def exp_marginal(x, x_mu, v0, sigma_v0):
    d = np.abs(x - x_mu)
    if d <= v0 ** 2 / (4 * sigma_v0):
        # v_square = 0.5 * v0 ** 2 - sigma_v0 * d - 0.5 * v0 * np.sqrt(v0 ** 2 - 4 * sigma_v0 * d)
        v_square = (0.5 * v0 - 0.5 * np.sqrt(v0 ** 2 - 4 * sigma_v0 * d))**2
        return np.exp(-d ** 2 / v_square)
    else:
       return None




v_expfun = np.vectorize(expfun)
v_exp_marginal = np.vectorize(exp_marginal)


def basic_explore():
    """
    This explore resembles Example8 in lixin wang's paper. Here  the uncertainty of the
    bandwidth is not zero mean, i.e., it has a center:the estimated bandwidth from data
    So I have a new formula for the marginal fuzzy set.
    :return:
    """
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle("1 several bandwidth", fontsize=20)
    # plot the primary membership function of x. sigma_x represents the bandwidth, we vary
    # this parameter to see the variation of membership functio
    primary_ax = axs[0]
    x = np.r_[0:25:1000j]
    x_mu = 12.5
    sigma_x = np.r_[1:4:4j]
    for i, sigma_x_i in enumerate(sigma_x):
        primary_ax.plot(x, v_expfun(x, x_mu, sigma_x_i), '--', color=colors[i])
    # plot the uncertainty of the estimated bandwidth
    secondary_ax = axs[1]
    v = np.r_[0:5:100j]
    v0 = 2.5  # the estimated bandwidth from data
    sigma_v0 = np.r_[0.1:5:4j]  # standard deviation (or uncertainty) of the bandwidth
    for i, sigma_v0_i in enumerate(sigma_v0):
        secondary_ax.plot(v, v_expfun(v, v0, sigma_v0_i), '.-', color=colors[i])
    # plot the marginal fuzzy set (also called membership function), we vary
    # the hyper-parameter sigma_v0 to see its influence
    marginal_ax = axs[2]
    for i, sigma_v0_i in enumerate(sigma_v0):
        marginal_ax.plot(x, v_exp_marginal(x, x_mu, v0, sigma_v0_i), '--', color=colors[i])
    for ax in axs:
        ax.set_ylim([0, 1.3])
    return None


basic_explore()

plt.show()
