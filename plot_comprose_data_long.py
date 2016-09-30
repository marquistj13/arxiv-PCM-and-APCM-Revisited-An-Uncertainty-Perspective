# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap

# discrete color scheme
cMap = ListedColormap(['blue', 'green', 'yellow', 'red', 'black'])

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('ggplot')

raw_data1 = np.load(r'./alpha_cut_sigmaV_long.npz')
alpha_cut1, sigma_v1, data1 = raw_data1['alpha_cut'], raw_data1['sigma_v'], raw_data1['results']
raw_data2 = np.load(r'./alpha_cut_sigmaV_long2.npz')
alpha_cut2, sigma_v2, data2 = raw_data2['alpha_cut'], raw_data2['sigma_v'], raw_data2['results']

# in raw_data1,the range of sigma_v1is [0.01,2] the step of sigma_v1 is 0.01, we need to sub-sample it.
sigma_v1=sigma_v1[9::10]#result: [0.1,0.2,...,1.9]
# we also need to sub-sample the corresponding column of data1
data1=data1[:,9::10]

#compine the two data sets
sigma_v=np.hstack((sigma_v1,sigma_v2))
alpha_cut=alpha_cut1 # the two are the same
print data1.shape,data2.shape
data=np.hstack((data1,data2))

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
# ax.invert_yaxis()

#lebels
column_labels = map(str,alpha_cut)
row_labels = map(str,sigma_v)
ax.set_xticklabels(column_labels, minor=False)
ax.set_yticklabels(row_labels, minor=False)
plt.show()
