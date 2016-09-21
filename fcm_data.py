# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from apcm import apcm
colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

def _generateTestData():
    #测试数据来自http://pythonhosted.org/scikit-fuzzy/auto_examples/plot_cmeans.html
    # Define three cluster centers
    centers = [[4, 2],
               [1, 7],
               [5, 6]]

    # Define three cluster sigmas in x and y, respectively
    sigmas = [[0.8, 0.3],
              [0.3, 0.5],
              [1.1, 0.7]]

    # Generate test data
    np.random.seed(42)  # Set seed for reproducibility
    xpts = np.zeros(1)
    ypts = np.zeros(1)
    labels = np.zeros(1)
    for i, ((xmu, ymu), (xsigma, ysigma)) in enumerate(zip(centers, sigmas)):
        xpts = np.hstack((xpts, np.random.standard_normal(200) * xsigma + xmu))
        ypts = np.hstack((ypts, np.random.standard_normal(200) * ysigma + ymu))
        labels = np.hstack((labels, np.ones(200) * i))

    # Visualize the test data
    fig0, ax0 = plt.subplots()
    for label in range(3):
        ax0.plot(xpts[labels == label], ypts[labels == label], '.',
                 color=colors[label])
    ax0.set_title('Test data: 200 points x3 clusters.')
    return np.r_['1,2,0',xpts,ypts]
if __name__=='__main__':
    X=_generateTestData()
    fig,ax=plt.subplots()
    clf=apcm(X,3,1,ax=ax,x_lim=(0,8),y_lim=(0,9))
    # we should set "blit=False,repeat=False" or the program would fail. "init_func=clf.init_animation" plot the
    # background of each frame There is not much point to use blit=True, if most parts of your plot should be
    # refreshed. see http://stackoverflow.com/questions/14844223/python-matplotlib-blit-to-axes-or-sides-of-the
    # -figure
    # To begin with, if you're chaining the ticks, etc, there isn't much point in using blitting. Blitting is
    #  just a way to avoid re-drawing everything if only some things are changing. If everything is changing,
    # there's no point in using blitting. Just re-draw the plot.
    anim = animation.FuncAnimation(fig, clf, frames=clf.fit,
                                   init_func=clf.init_animation, interval=700, blit=False,repeat=False)

    plt.show()
    pass