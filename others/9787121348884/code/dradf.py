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

rd = np.random.rand(10, 10)
plt.pcolor(rd, cmap="BuPu")
plt.colorbar()
plt.title("模拟图的颜色使用模式")
plt.show()
