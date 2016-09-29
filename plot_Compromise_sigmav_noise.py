# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from fs2_pcm_for_plot_use import pcm_fs2
from sklearn.datasets import make_blobs

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')


def _generateFig1():
    """
    Two close clusters, one big and the other small,
    :return:
    """

    x0, y0 = make_blobs(n_samples=400, n_features=2, centers=[[13, 13]], cluster_std=1, random_state=45)
    x1, y1 = make_blobs(n_samples=1000, n_features=2, centers=[[5, 0]], cluster_std=3.7, random_state=45)
    y1 += 1
    X = np.vstack((x0, x1))
    y = np.hstack((y0, y1))
    # Visualize the test data
    fig0, ax0 = plt.subplots()
    for label in range(2):
        ax0.plot(X[y == label][:, 0], X[y == label][:, 1], '.',
                 color=colors[label])
        ax0.set_xlim(-10, 20)
        ax0.set_ylim(-8, 16)
    # ax0.set_title('Test data: 200 points x3 clusters.')
    return X


if __name__ == '__main__':
    X = _generateFig1()
    theta_true = np.array([[13, 13], [5, 0]])
    fig, ax = plt.subplots()
    results = []
    for alpha_cut in np.arange(0.1, 1, 0.1):  # 0.1 to 0.9
        tmp_alpha_cut = []
        for sigma_v in np.arange(0.1, 2, 0.1):
            clf = pcm_fs2(X, 10, sigma_v, alpha_cut=alpha_cut, ax=ax, x_lim=(-10, 20), y_lim=(-8, 16)).fit()
            tmp_alpha_cut.append(len(clf.theta))
        results.append(tmp_alpha_cut)
    results = np.array(results)
    print results.shape
    np.savez(r'./alpha_cut_sigmaV', alpha_cut=np.arange(0.1, 1, 0.1), sigma_v=np.arange(0.1, 2, 0.1), results=results)

    plt.show()

    pass
