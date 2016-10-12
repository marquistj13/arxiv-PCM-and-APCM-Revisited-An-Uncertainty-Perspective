# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from fs2_pcm_for_plot_use import pcm_fs2
from sklearn.datasets import make_blobs

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('classic')

# the axis width also uses this value
plt.rcParams['axes.linewidth'] = 0.5


def _generateFig1():
    """
    Two close clusters, one big and the other small,
    :return:
    """

    x0, y0 = make_blobs(n_samples=1000, n_features=2, centers=[[5, 0]], cluster_std=3.7, random_state=45)
    x1, y1 = make_blobs(n_samples=200, n_features=2, centers=[[13, 13]], cluster_std=1, random_state=45)
    y1 += 1
    X = np.vstack((x0, x1))
    y = np.hstack((y0, y1))
    # # Visualize the test data
    # fig0, ax0 = plt.subplots()
    # for label in range(2):
    #     ax0.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
    #              color=colors[label])
    #     ax0.set_xlim(-10, 20)
    #     ax0.set_ylim(-8, 16)
    # # ax0.set_title('Test data: 200 points x3 clusters.')
    return X, y


def _generateFig6():
    """
    Two close clusters, one big and the other small,
    :return:
    """

    x0, y0 = make_blobs(n_samples=400, n_features=2, centers=[[1, 0]], cluster_std=0.2, random_state=45)
    x1, y1 = make_blobs(n_samples=400, n_features=2, centers=[[2.25, 1.5]], cluster_std=0.2, random_state=45)
    x2, y2 = make_blobs(n_samples=400, n_features=2, centers=[[1.75, 2]], cluster_std=0.2, random_state=45)
    y1 += 1
    y2 += 2
    X = np.vstack((x0, x1, x2))
    y = np.hstack((y0, y1, y2))
    # # Visualize the test data
    # fig0, ax0 = plt.subplots()
    # for label in range(3):
    #     ax0.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
    #              color=colors[label])
    # ax0.set_xlim(0.1, 3)
    # ax0.set_ylim(-0.75, 2.75)
    # # ax0.set_title('Test data: 200 points x3 clusters.')
    return X, y


if __name__ == '__main__':
    axs = []
    dpi = 300
    fig_size = (1.75, 1.75)
    fig1 = plt.figure(figsize=fig_size, dpi=dpi, num=1)
    ax = fig1.gca()
    axs.append(ax)
    fig2 = plt.figure(figsize=fig_size, dpi=dpi, num=2)
    ax = fig2.gca()
    axs.append(ax)
    fig3 = plt.figure(figsize=fig_size, dpi=dpi, num=3)
    ax = fig3.gca()
    axs.append(ax)
    fig4 = plt.figure(figsize=fig_size, dpi=dpi, num=4)
    ax = fig4.gca()
    axs.append(ax)

    marker_size = 1

    X, y = _generateFig1()
    # plot original fig1
    ax_fig1 = axs[0]
    for label in range(2):
        ax_fig1.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
                     color=colors[label], markersize=marker_size, label="Cluster %d" % (label + 1))
    ax_fig1.set_xlim(-10, 20)
    ax_fig1.set_ylim(-15, 20)
    lg=ax_fig1.legend(loc='upper left', fancybox=True, framealpha=0.8, prop={'size': 3})
    lg.get_frame().set_lw(0.4)
    # plot fcm init
    ax_fig2 = axs[1]
    cluster_num = 10
    clf = pcm_fs2(X, cluster_num, 1, alpha_cut=0, ax=ax, x_lim=(-10, 20), y_lim=(-8, 16))
    labels = clf.labels_init
    for label in range(cluster_num):
        ax_fig2.plot(X[labels == label][:, 0], X[labels == label][:, 1], '.',
                     color=colors[label], markersize=marker_size)
    ax_fig2.set_xlim(-10, 20)
    ax_fig2.set_ylim(-15, 20)
    # # ax_fig1.set_xticklabels(map(str, [-10,-5,0,5,10,15,20]), minor=False)
    # # ax_fig1.set_yticklabels(map(str, [-15,-10,-5,0,5,10,15,20]), minor=False)

    X, y = _generateFig6()
    # plot original fig6
    ax_fig3 = axs[2]
    for label in range(3):
        ax_fig3.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
                     color=colors[label], markersize=marker_size, label="Cluster %d" % (label + 1))
    ax_fig3.set_xlim(0.1, 3)
    ax_fig3.set_ylim(-0.75, 2.75)
    ax_fig3.set_xticklabels(map(str, ['', 0.5, 1, 1.5, 2, 2.5, 3]), minor=False)
    ax_fig3.set_yticklabels(map(str, ['', -0.5, 0, 0.5, 1, 1.5, 2, 2.5]), minor=False)
    lg=ax_fig3.legend(loc='upper left', fancybox=True, framealpha=0.8, prop={'size': 3})
    lg.get_frame().set_lw(0.4)

    # plot fcm init
    ax_fig4 = axs[3]
    cluster_num = 10
    clf = pcm_fs2(X, cluster_num, 1, alpha_cut=0, ax=ax, x_lim=(0.1, 3), y_lim=(-0.75, 2.75))
    labels = clf.labels_init
    for label in range(cluster_num):
        ax_fig4.plot(X[labels == label][:, 0], X[labels == label][:, 1], '.',
                     color=colors[label], markersize=marker_size)
    ax_fig4.set_xlim(0.1, 3)
    ax_fig4.set_ylim(-0.75, 2.75)
    ax_fig4.set_xticklabels(map(str, ['', 0.5, 1, 1.5, 2, 2.5, 3]), minor=False)
    ax_fig4.set_yticklabels(map(str, ['', -0.5, 0, 0.5, 1, 1.5, 2, 2.5]), minor=False)

    for _, axi in np.ndenumerate(axs):
        # Hide the right and top spines
        axi.spines['right'].set_visible(False)
        axi.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        axi.yaxis.set_ticks_position('left')
        axi.xaxis.set_ticks_position('bottom')
        # spine length
        axi.tick_params(length=1)
        # # font size
        # axi.set_xticklabels(axi.get_xticks(), minor=False, fontsize=3)
        # axi.set_yticklabels(axi.get_yticks(), minor=False, fontsize=3)  # same fontsize as xaxis
    for _, ax in np.ndenumerate(axs):
        zed = [tick.label.set_fontsize(4) for tick in ax.xaxis.get_major_ticks()]
        zed = [tick.label.set_fontsize(4) for tick in ax.yaxis.get_major_ticks()]

    plt.figure(1)
    plt.savefig(r".\img\fig1_ori.png", dpi=dpi, bbox_inches='tight')
    plt.figure(2)
    plt.savefig(r".\img\fig1_init.png", dpi=dpi, bbox_inches='tight')
    plt.figure(3)
    plt.savefig(r".\img\fig6_ori.png", dpi=dpi, bbox_inches='tight')
    plt.figure(4)
    plt.savefig(r".\img\fig6_init.png", dpi=dpi, bbox_inches='tight')
    plt.show()

    pass
