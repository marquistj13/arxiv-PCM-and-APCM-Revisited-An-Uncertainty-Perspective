# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

data = np.load(r'./alpha_cut_sigmaV.npz')
# data = np.load(r'./alpha_cut_sigmaV_long.npz')
alpha_cut, sigma_v, results = data['alpha_cut'], data['sigma_v'], data['results']

# # plt.hist2d(alpha_cut,sigma_v,)
# fig, ax = plt.subplots()
#
# # cax = ax.imshow(results, interpolation='nearest', cmap=cm.coolwarm)
# cax = ax.imshow(results)
# ax.set_title('Gaussian noise with vertical colorbar')
#
# # Add colorbar, make sure to specify tick locations to match desired ticklabels
# cbar = fig.colorbar(cax)
# # cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar

X,Y=np.meshgrid(alpha_cut,sigma_v)
plt.scatter(x=X,y=Y,c=results)
# plt.pcolor(results)
# plt.imshow(results)
plt.colorbar()
print results
# plt.hexbin(X.ravel(),Y.ravel(),C=results.ravel(),gridsize=10)
plt.show()