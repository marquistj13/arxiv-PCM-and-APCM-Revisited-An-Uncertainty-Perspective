# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pcm_fs2 import pcm_fs2
from sklearn.datasets import make_blobs

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('classic')


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
    # ax0.set_title('Test data: 200 points x3 clusters.')
    return X, y


if __name__ == '__main__':
    X, y = _generateFig6()
    marker_size = 4
    dpi = 300
    fig_size = None
    # plot ori data and save
    fig1 = plt.figure(figsize=fig_size, dpi=dpi, num=1)
    ax_fig1 = fig1.gca()
    for label in range(3):
        ax_fig1.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
                     color=colors[label], markersize=marker_size, label="Cluster %d" % (label + 1))
    ax_fig1.set_xlim(0.1, 3)
    ax_fig1.set_ylim(-0.75, 2.75)
    lg = ax_fig1.legend(loc='upper left', fancybox=True, framealpha=0.5, prop={'size': 8})
    ax_fig1.set_title("Original Dataset")
    plt.savefig(r".\video\fig6_ori.png", dpi=dpi, bbox_inches='tight')
    # plot animation and save
    fig2 = plt.figure(figsize=fig_size, dpi=dpi, num=2)
    ax = fig2.gca()
    n_cluster, sigma_v, alpha_cut = 10, 4, 0.9
    clf = pcm_fs2(X, n_cluster, sigma_v, alpha_cut=alpha_cut, ax=ax,  x_lim=(0.1, 3), y_lim=(-0.75, 2.75))
    # we should set "blit=False,repeat=False" or the program would fail. "init_func=clf.init_animation" plot the
    # background of each frame There is not much point to use blit=True, if most parts of your plot should be
    # refreshed. see http://stackoverflow.com/questions/14844223/python-matplotlib-blit-to-axes-or-sides-of-the
    # -figure
    # To begin with, if you're chaining the ticks, etc, there isn't much point in using blitting. Blitting is
    #  just a way to avoid re-drawing everything if only some things are changing. If everything is changing,
    # there's no point in using blitting. Just re-draw the plot.
    anim = animation.FuncAnimation(fig2, clf, frames=clf.fit,
                                   init_func=clf.init_animation, interval=700, blit=True, repeat=False)
    anim.save(r'.\video\fig6_n_%d_sigmav_%.1f_alpha_%.1f.mp4' % (n_cluster, sigma_v, alpha_cut),
              fps=None, extra_args=['-vcodec', 'libx264'], dpi='figure')

    plt.show()
    pass
