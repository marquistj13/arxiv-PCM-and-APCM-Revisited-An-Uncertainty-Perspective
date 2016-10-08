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

def _generateFig1_400_points():
    """
    Two close clusters, one big and the other small,
    :return:
    """

    x0, y0 = make_blobs(n_samples=1000, n_features=2, centers=[[5, 0]], cluster_std=3.7, random_state=45)
    x1, y1 = make_blobs(n_samples=400, n_features=2, centers=[[13, 13]], cluster_std=1, random_state=45)
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


if __name__ == '__main__':
    axs = []
    dpi = 300
    fig_size = (1.2, 1.2)
    fig1 = plt.figure(figsize=fig_size, dpi=dpi, num=1)
    ax = fig1.gca()
    axs.append(ax)

    marker_size = 0.4

    X, y = _generateFig1_400_points()
    # 1st case: alpha_cut=0.1
    ax_fig1 = axs[0]
    cluster_num = 2
    clf = pcm_fs2(X, cluster_num, 4, alpha_cut=0, ax=ax, x_lim=(-10, 20), y_lim=(-8, 16)).fit()
    labels = np.argmax(clf.u, axis=1)
    print clf.m
    for label in range(clf.m):
        ax_fig1.plot(X[labels == label][:, 0], X[labels == label][:, 1], '.',
                     color=colors[label], markersize=marker_size,
                     label="Cluster {0} with $\eta$={1:.2f}".format(label,clf.ita[label]))
        # centers,
        [ax_fig1.plot(clf.theta[label][0], clf.theta[label][1], 'rs', markersize=4*marker_size)[0] for _ in range(clf.m)]
        # add circles to indication the standard deviation, i.e., the influence of each cluster
        [ax_fig1.add_patch(plt.Circle((clf.theta[label][0], clf.theta[label][1]), radius=clf.ita[label], color='k',
                                 fill=None, lw=0.5)) for _ in range(clf.m)]
        print label,clf.ita[label]
    ax_fig1.set_xlim(-10, 20)
    ax_fig1.set_ylim(-15, 20)
    lg=ax_fig1.legend(loc='upper left', fancybox=True, framealpha=0.5, prop={'size': 2})
    lg.get_frame().set_lw(0.4)
    # # ax_fig1.set_xticklabels(map(str, [-10,-5,0,5,10,15,20]), minor=False)
    # # ax_fig1.set_yticklabels(map(str, [-15,-10,-5,0,5,10,15,20]), minor=False)



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
        zed = [tick.label.set_fontsize(3) for tick in ax.xaxis.get_major_ticks()]
        zed = [tick.label.set_fontsize(3) for tick in ax.yaxis.get_major_ticks()]

    plt.figure(1)
    plt.show()

    pass
