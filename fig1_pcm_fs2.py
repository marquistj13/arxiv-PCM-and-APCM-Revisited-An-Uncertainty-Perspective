# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pcm_fs2 import pcm_fs2
from sklearn.datasets import make_blobs
colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

def _generateFig1():
    """
    Two close clusters, one big and the other small,
    :return:
    """

    x0,y0=make_blobs(n_samples=400,n_features=2,centers=[[13,13]],cluster_std=1,random_state=45)
    x1,y1=make_blobs(n_samples=1000,n_features=2,centers=[[5,0]],cluster_std=3.7,random_state=45)
    y1+=1
    X=np.vstack((x0,x1))
    y=np.hstack((y0,y1))
    # Visualize the test data
    fig0, ax0 = plt.subplots()
    for label in range(2):
        ax0.plot(X[y == label][:,0], X[y == label][:,1], '.',
                 color=colors[label])
        ax0.set_xlim(-10,20)
        ax0.set_ylim(-8,16)
    # ax0.set_title('Test data: 200 points x3 clusters.')
    return X
if __name__=='__main__':
    X=_generateFig1()
    fig,ax=plt.subplots()
    clf=pcm_fs2(X,2,4,alpha_cut=0.0,ax=ax,x_lim=(-10,20),y_lim=(-8,16))
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