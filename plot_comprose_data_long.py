# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, mpl
from matplotlib.colors import ListedColormap
from matplotlib.ticker import FuncFormatter

# this plot mainly refer to
# http://stackoverflow.com/questions/9707676/defining-a-discrete-colormap-for-imshow-in-matplotlib
# and http://stackoverflow.com/questions/7229971/2d-grid-data-visualization-in-python
# discrete color scheme
cMap = ListedColormap(['green', 'blue', 'yellow', 'red', 'black'])
# cMap = ListedColormap(['blue', 'green', 'yellow',  'black'])
bounds = [0, 1.1, 2.1, 3.1, 4.1, 10.1]
norm = mpl.colors.BoundaryNorm(bounds, cMap.N)

colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
# plt.style.use('ggplot')

raw_data1 = np.load(r'./alpha_cut_sigmaV_long.npz')
alpha_cut1, sigma_v1, data1 = raw_data1['alpha_cut'], raw_data1['sigma_v'], raw_data1['results']
raw_data2 = np.load(r'./alpha_cut_sigmaV_long2.npz')
alpha_cut2, sigma_v2, data2 = raw_data2['alpha_cut'], raw_data2['sigma_v'], raw_data2['results']
raw_data3 = np.load(r'./alpha_cut_sigmaV_long3.npz')
alpha_cut3, sigma_v3, data3 = raw_data3['alpha_cut'], raw_data3['sigma_v'], raw_data3['results']
raw_data4 = np.load(r'./alpha_cut_sigmaV_long4.npz')
alpha_cut4, sigma_v4, data4 = raw_data4['alpha_cut'], raw_data4['sigma_v'], raw_data4['results']
# in raw_data1,the range of sigma_v1is [0.01,2] the step of sigma_v1 is 0.01, we need to sub-sample it.
sigma_v1 = sigma_v1[9::10]  # result: [0.1,0.2,...,1.9]
# we also need to sub-sample the corresponding column of data1
data1 = data1[:, 9::10]

# compine the two data sets
sigma_v = np.hstack((sigma_v1, sigma_v2, sigma_v3, sigma_v4))
alpha_cut = alpha_cut1  # the two are the same
data = np.hstack((data1, data2, data3, data4))
print data.shape
# print alpha_cut
# print data[4, :]

data = data.T
data[data >= 5] = 5
X, Y = np.meshgrid(alpha_cut, sigma_v)
# plt.scatter(x=X,y=Y,c=results)

fig, ax = plt.subplots(figsize=(3.5, 2.5), dpi=300, facecolor='white')
dpi = fig.dpi  # extract the dpi value
# fig.set_size_inches(3.5, 2.5)  # physical size

heatmap = ax.pcolor(data, cmap=cMap, norm=norm)
# legend
cbar = plt.colorbar(heatmap, cmap=cMap, norm=norm, boundaries=bounds)
# cbar = plt.colorbar(heatmap, cmap=cMap, norm=norm, boundaries=bounds, ticks=[1, 2, 3, 4, 5])
cbar.ax.get_yaxis().set_ticks([])
cbar.ax.get_yaxis().set_ticks([])
# for j, lab in enumerate([r'$m_{final}=1$', '$m_{final}=2$', '$m_{final}=3$', '$m_{final}=4$', '$m_{final}\geq5$']):
for j, lab in enumerate([r'$m=1$', '$m=2$', '$m=3$', '$m=4$', '$m\geq5$']):
    cbar.ax.text(2.3, (2 * j + 1) / 10.0, lab, ha='center', va='center', fontname='Times New Roman',
                 fontsize='xx-small')
cbar.ax.get_yaxis().labelpad = 15

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(data.shape[0])[9::10] + 0.5, minor=False)

# labels
# we know the 'column' is 0.1 to 0.95, so we manullary set it, and remove the '0' on the left
# column_labels = map(str, alpha_cut)
column_labels = map(lambda x:str(x).lstrip('0'), np.arange(.1,1,0.05))
# we know the 'row' is 0 to 16, so we manullary set it
# row_labels = map(str, sigma_v[9::10])
row_labels = map(str, range(1,17,1))
ax.set_xticklabels(column_labels, minor=False, fontsize=4)
ax.set_yticklabels(row_labels, minor=False, fontsize=4)

# remove extra 0 in the ticks
formatter = FuncFormatter(lambda x, pos: str(x).lstrip('0'))
for _, axi in np.ndenumerate([ax]):
    # axi.yaxis.set_major_formatter(formatter) #it doesn't work for yaxis,I don't know why
    # axi.xaxis.set_major_formatter(formatter) # also not works
    pass
for _, axi in np.ndenumerate([ax]):
    # Hide the right and top spines
    axi.spines['right'].set_visible(False)
    axi.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    axi.yaxis.set_ticks_position('left')
    axi.xaxis.set_ticks_position('bottom')

# It has 161 points in the yaxis,we limit it to 160(or 161) to avoid space in the plot
# See http://stackoverflow.com/questions/19184500/python-matplotlib-pcolor-blank-space
ax.set_ylim((0, 160))

plt.savefig(r"./img/plot_comprose_data_long.png",dpi=fig.dpi,bbox_inches="tight")
plt.show()

