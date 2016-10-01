# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, mpl
from matplotlib.colors import ListedColormap
from matplotlib.ticker import FuncFormatter

colors = ['m', 'ForestGreen', 'c', 'b', 'orange', 'g', 'r', 'y', 'k', 'Brown']
# plt.style.use('grayscale')

raw_data = np.load(r'./sigmaV_alpha_cut.npz')
alpha_cut, sigma_v, data = raw_data['alpha_cut'], raw_data['sigma_v'], raw_data['results']

fig, ax = plt.subplots(figsize=(3.5, 3.5), dpi=300, facecolor='white')
dpi = fig.dpi  # extract the dpi value
# fig.set_size_inches(3.5, 2.5)  # physical size
# for i, data_i in enumerate(data):
#     ax.plot(data_i[:, 0], data_i[:, 1], '.-', color=colors[i])
marker_size = 3
# # with marker
# data_0=data[0]
# ax.plot(data_0[:, 0], data_0[:, 1], 'd-', color=colors[0],markersize=marker_size,label=r"$\alpha_{cut}=0.1$")
# data_1=data[1]
# ax.plot(data_1[:, 0], data_1[:, 1], '*-', color=colors[1],markersize=marker_size,label=r"$\alpha_{cut}=0.3$")
# data_2=data[2]
# ax.plot(data_2[:, 0], data_2[:, 1], '^-', color=colors[2],markersize=marker_size,label=r"$\alpha_{cut}=0.5$")
# without marker
data_0 = data[0]
ax.plot(data_0[:, 0], data_0[:, 1], '.-', color=colors[0], markersize=marker_size, label=r"$\alpha=0.1$")
data_1 = data[1]
ax.plot(data_1[:, 0], data_1[:, 1], '.-', color=colors[1], markersize=marker_size, label=r"$\alpha=0.3$")
data_2 = data[2]
ax.plot(data_2[:, 0], data_2[:, 1], '.-', color=colors[2], markersize=marker_size, label=r"$\alpha=0.5$")

ax.legend(loc='upper left', fancybox=True, framealpha=0.5, prop={'size': 5})

ax.axhline(y=7, xmin=0, xmax=16, color='k', ls='--')

# apcm_color, pcm_color = 'r', 'blue'
apcm_color, pcm_color = 'k', 'k'
plt.fill_between(np.linspace(0, 16, 500), np.zeros(500), np.zeros(500) + 7, color=apcm_color, alpha=0.05)
plt.fill_between(np.linspace(0, 16, 500), np.zeros(500) + 7, np.zeros(500) + 14, color=pcm_color, alpha=0.05)
ax.text(1, 4, 'APCM', color=apcm_color)
ax.text(1, 9, 'PCM', color=pcm_color)
for _, axi in np.ndenumerate([ax]):
    # Hide the right and top spines
    axi.spines['right'].set_visible(False)
    axi.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    axi.yaxis.set_ticks_position('left')
    axi.xaxis.set_ticks_position('bottom')
for _, ax in np.ndenumerate([ax]):
    zed = [tick.label.set_fontsize(6) for tick in ax.xaxis.get_major_ticks()]
    zed = [tick.label.set_fontsize(6) for tick in ax.yaxis.get_major_ticks()]

plt.savefig(r"./img/plot_sigmaV_data.png", dpi=fig.dpi, bbox_inches="tight")
plt.show()
