"""
@Title        : 
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-17 21:03:38
@Description  : 
"""

import matplotlib.patheffects as pes
from matplotlib.sankey import Sankey
from matplotlib.ticker import FormatStrFormatter
from calendar import day_name
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

font_style = dict(color="saddlebrown", weight="semibold", size=16)
line_marker_style = dict(
    linestyle=":",
    linewidth=2,
    color="cornflowerblue",
    markerfacecoloralt="lightgrey",
    marker="o",
    markersize=18,
)
fig = plt.figure()
ax = fig.add_subplot(111)
fill_style_list = ["full", "left", "right", "bottom", "top", "none"]
x = np.arange(3, 11, 1)
y = np.linspace(1, 1, 8)
for i, fs in enumerate(fill_style_list):
    ax.text(0, i + 0.4, "'{}'".format(fs), **font_style)
    ax.plot(x, (i + 0.5) * y, fillstyle=fs, **line_marker_style)
ax.set_xlim(-1, 11)
ax.set_ylim(0, 6)
ax.margins(0.3)
# ax.set_xticks([])
# ax.set_yticks([])
ax.axis("off")
plt.title("标记填充样式的设置方法")
plt.show()
