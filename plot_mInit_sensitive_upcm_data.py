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

    x0, y0 = make_blobs(n_samples=200, n_features=2, centers=[[13, 13]], cluster_std=1, random_state=45)
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
    results = []  # store the final result
    for alpha_cut in [0, 0.1, 0.3, 0.5]:
        print "alpha_cut=", alpha_cut
        tmp_alpha_cut = []  # store the result of each alpha_cut
        for m_ini in [2, 5, 8, 11, 13, 16, 19]:
            print "m_ini=", m_ini
            tmp_m_ini = []  # store the m of each  m_ini
            for sigma_v in np.r_[0:15:100j]:
                # for sigma_v in np.arange(1, 20):
                clf = pcm_fs2(X, m_ini, sigma_v, alpha_cut=alpha_cut, ax=ax, x_lim=(-10, 20), y_lim=(-8, 16)).fit()
                m_final = clf.m
                tmp_m_ini.append(m_final)  # store the m of each  m_ini
            tmp_alpha_cut.append(tmp_m_ini)  # store the result of each alpha_cut
        results.append(tmp_alpha_cut)  # store the final result
    results = np.array(results)  # shape: n_alpha_cut x n_m_ini  x n_sigma_v
    np.savez(r'./data/plot_mInit_sensitive_upcm', alpha_cut=[0, 0.1, 0.3, 0.5], m_ini=[2, 5, 8, 11, 13, 16, 19],
             sigma_v=np.r_[0:15:100j],results=results)
    print results.shape
    # for i, result_i in enumerate(results):
    #     ax.plot(result_i[:, 0], result_i[:, 1], '.-', color=colors[i])
    # plt.show()

    pass
