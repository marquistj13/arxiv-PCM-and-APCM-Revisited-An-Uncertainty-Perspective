# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
# plt.style.use('ggplot')


def expfun(x, mu, sigma):
    return np.exp(-(x - mu) ** 2 / sigma ** 2)


def exp_marginal(x, x_mu, v0, sigma_v0):
    d = np.abs(x - x_mu)
    v_square = 0.5 * v0 ** 2 + sigma_v0 * d + 0.5 * v0 * np.sqrt(v0 ** 2 + 4 * sigma_v0 * d)
    return np.exp(-d ** 2 / v_square)


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
    fig.suptitle("1 several bandwidth",fontsize=20)
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
    return None


def specific_case():
    """
    This function is actually the same with the above basic_explore() except that I limit
    the data range for my use. In fact, function basic_explore() is more general.
    Below is the comment adapted from basic_explore():
    This explore resembles Example8 in lixin wang's paper. Here  the uncertainty of the
    bandwidth is not zero mean, i.e., it has a center:the estimated bandwidth from data
    So I have a new formula for the marginal fuzzy set.
    :return:
    """
    fig, axs = plt.subplots(1, 3, figsize=(4.5, 1.5), dpi=300, facecolor='white')
    

    # plot the primary membership function of x. sigma_x represents the bandwidth, we vary
    # this parameter to see the variation of membership functio
    marker_size = 0.3
    line_width=0.1
    label_fontsize=4
    title_fontsize=4
    primary_ax = axs[0]
    x = np.r_[0:25:1000j]
    x_mu = 12.5
    sigma_x = np.r_[1:4:4j]
    # for i, sigma_x_i in enumerate(sigma_x):
    #     primary_ax.plot(x, v_expfun(x, x_mu, sigma_x_i), '.-', color=colors[i])
    primary_ax.plot(x, v_expfun(x, x_mu, 2.5), '.-', color=colors[0], markersize=marker_size,lw=line_width)
    # plot the uncertainty of the estimated bandwidth
    secondary_ax = axs[1]
    v = np.r_[0:5:100j]
    v0 = 2.5  # the estimated bandwidth from data
    sigma_v0 = np.r_[0.5:5:4j]  # standard deviation (or uncertainty) of the bandwidth
    for i, sigma_v0_i in enumerate(sigma_v0):
        secondary_ax.plot(v, v_expfun(v, v0, sigma_v0_i), '.-', color=colors[i], markersize=marker_size,lw=line_width)
    secondary_ax.set_ylabel(r"$\mu_v(v)$",fontsize = label_fontsize)
    secondary_ax.set_title("Secondary Fuzziness",fontsize = title_fontsize)
    # plot the marginal fuzzy set (also called membership function), we vary
    # the hyper-parameter sigma_v0 to see its influence
    marginal_ax = axs[2]
    for i, sigma_v0_i in enumerate(np.r_[[0],0.5:2:4j]):# add sigma_v0_i=0 to indicate the original MF
        marginal_ax.plot(x, v_exp_marginal(x, x_mu, v0, sigma_v0_i), '.-', color=colors[i], markersize=marker_size,lw=line_width)
    for ax in axs:
        ax.set_ylim([0, 1.3])

    for _, axi in np.ndenumerate(axs):
        # Hide the right and top spines
        axi.spines['right'].set_visible(False)
        axi.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        axi.yaxis.set_ticks_position('left')
        axi.xaxis.set_ticks_position('bottom')
    for _, ax in np.ndenumerate(axs):
        zed = [tick.label.set_fontsize(4) for tick in ax.xaxis.get_major_ticks()]
        zed = [tick.label.set_fontsize(4) for tick in ax.yaxis.get_major_ticks()]
    plt.savefig(r"./img/plot_type2_mf.png", dpi=fig.dpi, bbox_inches="tight")
    return None
# basic_explore()
specific_case()

plt.show()
