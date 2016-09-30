# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap

# discrete color scheme
cMap = ListedColormap(['blue', 'green', 'yellow', 'red', 'black'])

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

raw_data = np.load(r'./alpha_cut_sigmaV_long.npz')
alpha_cut, sigma_v, data = raw_data['alpha_cut'], raw_data['sigma_v'], raw_data['results']
data=data.T
data[data >= 5] = 5
X, Y = np.meshgrid(alpha_cut, sigma_v)
# plt.scatter(x=X,y=Y,c=results)

fig, ax = plt.subplots()
heatmap=ax.pcolor(data, cmap=cMap)
#legend
cbar = plt.colorbar(heatmap)
cbar.ax.get_yaxis().set_ticks([])
cbar.ax.get_yaxis().set_ticks([])
for j, lab in enumerate(['$2$','$3$','$4$','$>=5$']):
    cbar.ax.text(.5, (2 * j + 1) / 8.0, lab, ha='center', va='center')
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('# of contacts', rotation=270)


# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
ax.invert_yaxis()

#lebels
column_labels = map(str,alpha_cut)
row_labels = map(str,sigma_v)
ax.set_xticklabels(column_labels, minor=False)
ax.set_yticklabels(row_labels, minor=False)


# plt.grid()

# plt.hexbin(X.ravel(),Y.ravel(),C=results.ravel(),gridsize=10)
plt.show()
