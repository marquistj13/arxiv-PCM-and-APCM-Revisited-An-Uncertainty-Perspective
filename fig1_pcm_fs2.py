# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pcm_fs2 import pcm_fs2
from sklearn.datasets import make_blobs

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('classic')


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


if __name__ == '__main__':
    X, y = _generateFig1()
    marker_size = 4
    dpi = 300
    fig_size = None
    # plot ori data and save
    fig1 = plt.figure(figsize=fig_size, dpi=dpi, num=1)
    ax_fig1 = fig1.gca()
    for label in range(2):
        ax_fig1.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
                     color=colors[label], markersize=marker_size, label="Cluster %d" % (label + 1))
    ax_fig1.set_xlim(-10, 20)
    ax_fig1.set_ylim(-15, 20)
    lg = ax_fig1.legend(loc='upper left', fancybox=True, framealpha=0.5, prop={'size': 8})
    ax_fig1.set_title("Original Dataset")
    plt.savefig(r".\video\fig1_ori.png", dpi=dpi, bbox_inches='tight')
    # plot animation and save
    fig2 = plt.figure(figsize=fig_size, dpi=dpi, num=2)
    ax = fig2.gca()
    n_cluster, sigma_v, alpha_cut = 10, 2, 0
    clf = pcm_fs2(X, n_cluster, sigma_v, alpha_cut=alpha_cut, ax=ax, x_lim=(-10, 20), y_lim=(-8, 16))
    # we should set "blit=False,repeat=False" or the program would fail. "init_func=clf.init_animation" plot the
    # background of each frame There is not much point to use blit=True, if most parts of your plot should be
    # refreshed. see http://stackoverflow.com/questions/14844223/python-matplotlib-blit-to-axes-or-sides-of-the
    # -figure
    # To begin with, if you're chaining the ticks, etc, there isn't much point in using blitting. Blitting is
    #  just a way to avoid re-drawing everything if only some things are changing. If everything is changing,
    # there's no point in using blitting. Just re-draw the plot.
    anim = animation.FuncAnimation(fig2, clf, frames=clf.fit,
                                   init_func=clf.init_animation, interval=700, blit=True, repeat=False)
    anim.save(r'.\video\fig1_n_%d_sigmav_%.1f_alpha_%.1f.mp4' % (n_cluster, sigma_v, alpha_cut),
              fps=None, extra_args=['-vcodec', 'libx264'], dpi='figure')

    plt.show()
    pass
