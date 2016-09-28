# -*- coding: utf-8 -*-
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import matplotlib.animation as animation

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')


def exp_marginal(d, v0, sigma_v0):
    v_square = 0.5 * v0 ** 2 + sigma_v0 * d + 0.5 * v0 * np.sqrt(v0 ** 2 + 4 * sigma_v0 * d)
    return np.exp(-d ** 2 / v_square)


v_exp_marginal = np.vectorize(exp_marginal)


class hpcm_fs2():
    def __init__(self, X, m, sig_v0):
        """
        :param X: scikit-learn form, i.e., pf shape (n_samples, n_features)
        :param m: NO.of initial clusters
        :param sig_v0:
        :return:
        """
        self.x = X
        self.m = m
        self.m_ori = m  # the original number of clusters specified
        self.sig_v0 = float(sig_v0)

        # use fcm to initialise the clusters
        self.init_theta_ita()
        pass

    def init_theta_ita(self):
        x_tmp = self.x.T  # becasue skfuzzy is converted from matlab, the data should be of (n_features, n_samples)
        cntr, u_orig, _, _, _, _, _ = fuzz.cluster.cmeans(x_tmp, self.m, 2, error=0.005, maxiter=1000, seed=45)
        # cntr, u_orig represent center,fuzzy c-partitioned matrix (membership matrix)
        u_orig = u_orig.T  # convert back to scikit-learn form (n_samples, n_features)
        # I'm confused that the returned cntr is already (n_samples, n_features) and doesn't need the transpose
        # plot the fcm initialization
        labels = np.argmax(u_orig, axis=1)
        # initialize theta, i.e., the centers
        self.theta = cntr
        # now compute ita
        ita = np.zeros(self.m)
        for cntr_index in range(self.m):
            dist_2_cntr = map(np.linalg.norm, self.x - cntr[cntr_index])
            ita[cntr_index] = np.dot(dist_2_cntr, u_orig[:, cntr_index]) / sum(u_orig[:, cntr_index])
        self.ita = ita
        self.ita_hat = min(ita)
        pass

    def fit(self, center):
        center = np.array(center)
        dist_2_cntr = map(np.linalg.norm, self.x - center)
        u = v_exp_marginal(dist_2_cntr, self.ita_hat, self.sig_v0)
        return np.dot(u, dist_2_cntr) + self.ita_hat * sum(map(lambda x: x * np.log(x) - x, u))


def _generate1d():
    """
    :return:
    """
    np.random.seed(45)
    x0 = np.random.normal(loc=28, scale=10, size=(50, 1))
    x1 = np.random.normal(loc=67, scale=11, size=(50, 1))
    print x0.shape
    # Visualize the test data
    fig0, ax0 = plt.subplots()

    ax0.plot(x0, np.zeros(50), '.', color=colors[0])
    ax0.plot(x1, np.zeros(50), '.', color=colors[1])
    # ax0.set_title('Test data: 200 points x3 clusters.')
    return np.vstack((x0, x1))


if __name__ == '__main__':
    X = _generate1d()
    fig, ax = plt.subplots()
    clf = hpcm_fs2(X, 3, 0.00030)
    x = np.r_[0:90:500j]
    y = map(clf.fit, x)
    ax.plot(x, y)
    ax.plot(X[:50], np.zeros(50), '.', color=colors[0])
    ax.plot(X[50:], np.zeros(50), '.', color=colors[1])
    plt.show()
    pass
