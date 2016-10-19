# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
plt.style.use('classic')
# refer to http://matplotlib.org/examples/pylab_examples/fonts_demo.html for font_demo
font = FontProperties()
font.set_family('fantasy')
font.set_weight('bold')
font.set_size('x-large')
axs = []
dpi = 300
fig_size = (10,5)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=1, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = """We first look at a noisy dataset and notice the problem:
the small cluster is dragged by large clusters and then eliminated."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=2, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""This issue can be solved either by increasing our confidence in the
estimated bandwidth $\eta_j$, i.e., the bandwidth uncertainty parameter $\sigma_v$
decreases from $1$ to $0.5$."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=3, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""or solved by specifying a higher noise level $\alpha$=$0.2$ instead of $0.1$
so the points of large clusters have less nor no influence to adaption of
the small cluster."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=4, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""We will look at another well-separated dataset.
Next is the proper setting of prarameters."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=5, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""Increasing $\sigma_v$ from $1$ to $2$ causes the small cluster to be dragged by
the large cluster."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=6, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""Now we set $m_{ini}$=$10$, and the previous prameter setting still works fine."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=7, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""However, increasing $\sigma_v$ to $4$ will cause problems."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=8, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""We will look at another not well-separated dataset, so we should set
a high noise level $\alpha$.
Next is the proper setting of prarameters."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=9, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""Specifying a low noise level $\alpha$ will not work."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=10, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""Now we set $m_{ini}$=$10$.
A small $\sigma_v$ will not ensure small clusters in the same physical cluster
 to merge."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)

fig = plt.figure(figsize=fig_size, dpi=dpi, num=11, frameon=False)
ax = fig.gca()
axs.append(ax)
txt = r"""So we should specify a larger $\sigma_v$."""
ax.text(0., 0.4, txt, transform=ax.transAxes,fontproperties=font)


for axi in axs:
    axi.axis('off')

plt.figure(1)
plt.savefig(r".\video\fig8_n_10_sigmav_1.0_alpha_0.1.png", dpi=dpi)
plt.figure(2)
plt.savefig(r".\video\fig8_n_10_sigmav_0.5_alpha_0.1.png", dpi=dpi)
plt.figure(3)
plt.savefig(r".\video\fig8_n_10_sigmav_1.0_alpha_0.2.png", dpi=dpi)
plt.figure(4)
plt.savefig(r".\video\fig1_n_2_sigmav_1.0_alpha_0.0.png", dpi=dpi)
plt.figure(5)
plt.savefig(r".\video\fig1_n_2_sigmav_2.0_alpha_0.0.png", dpi=dpi)
plt.figure(6)
plt.savefig(r".\video\fig1_n_10_sigmav_2.0_alpha_0.0.png", dpi=dpi)
plt.figure(7)
plt.savefig(r".\video\fig1_n_10_sigmav_4.0_alpha_0.0.png", dpi=dpi)
plt.figure(8)
plt.savefig(r".\video\fig6_n_3_sigmav_3.0_alpha_0.9.png", dpi=dpi)
plt.figure(9)
plt.savefig(r".\video\fig6_n_3_sigmav_3.0_alpha_0.5.png", dpi=dpi)
plt.figure(10)
plt.savefig(r".\video\fig6_n_10_sigmav_3.0_alpha_0.9.png", dpi=dpi)
plt.figure(11)
plt.savefig(r".\video\fig6_n_10_sigmav_4.0_alpha_0.9.png", dpi=dpi)
# plt.show()
