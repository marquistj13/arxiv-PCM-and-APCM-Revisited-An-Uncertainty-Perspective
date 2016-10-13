# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, mpl
from matplotlib.colors import ListedColormap
from matplotlib.ticker import FuncFormatter

colors = ['m', 'ForestGreen', 'c', 'b', 'orange', 'g', 'r', 'y', 'k', 'Brown']
# plt.style.use('grayscale')

raw_data = np.load(r'./data/plot_mInit_sensitive_upcm.npz')
alpha_cut, m_ini, sigma_v, data = raw_data['alpha_cut'], raw_data['m_ini'], raw_data['sigma_v'], raw_data['results']
print data.shape
# alpha_cut = [0, 0.1, 0.3, 0.5]
# m_ini = [2, 5, 8, 11, 13, 16, 19]
# sigma_v = np.r_[0:15:100j]


fig, ax = plt.subplots(figsize=(3.5, 3.5), dpi=300, facecolor='white')
dpi = fig.dpi  # extract the dpi value
# fig.set_size_inches(3.5, 2.5)  # physical size
# for i, data_i in enumerate(data):
#     ax.plot(data_i[:, 0], data_i[:, 1], '.-', color=colors[i])
marker_size = 3

for i, data_i in enumerate(data[3][:]):
    ax.plot(sigma_v, data_i, '.-', color=colors[i], markersize=marker_size,
            label=r"$m_{ini}=%d$" % (m_ini[i]),alpha=0.7)

ax.legend(loc='lower right', fancybox=True, framealpha=0.5, prop={'size': 8})

for _, axi in np.ndenumerate([ax]):
    # Hide the right and top spines
    axi.spines['right'].set_visible(False)
    axi.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    axi.yaxis.set_ticks_position('left')
    axi.xaxis.set_ticks_position('bottom')
for _, ax in np.ndenumerate([ax]):
    zed = [tick.label.set_fontsize(8) for tick in ax.xaxis.get_major_ticks()]
    zed = [tick.label.set_fontsize(8) for tick in ax.yaxis.get_major_ticks()]
ax.tick_params(length=1)
plt.savefig(r"./img/plot_mInit_sensitive_upcm.png", dpi=fig.dpi, bbox_inches="tight")
plt.show()
