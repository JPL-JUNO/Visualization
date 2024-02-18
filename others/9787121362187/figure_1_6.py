"""
@File         : figure_1_6.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-18 23:05:17
@Email        : cuixuanstephen@gmail.com
@Description  : 综合案例：交叉间断型曲线的颜色填充
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2)
# subplot(121) data
x = np.linspace(0, 2, 500)
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(3 * np.pi * x)
# 有一部分数据没掩码处理了，显式为 --
y2 = np.ma.masked_greater(y2, 1.0)

ax[0].plot(x, y1, lw=1, ls="-", label="y1")
ax[0].plot(x, y2, lw=1, ls="-", label="y2")
ax[0].fill_between(x, y1, y2, where=y2 >= y1, facecolor="cornflowerblue", alpha=0.7)
# where y1>= y2
ax[0].fill_between(x, y1, y2, where=y2 <= y1, facecolor="darkred", alpha=0.7)
ax[0].set_xlim(0, 2)
ax[0].set_ylim(-1.2, 1.2)
ax[0].grid(ls=":", lw=1, color="gray", alpha=0.5)
ax[0].legend()

y = np.linspace(0, 2, 500)
x1 = np.sin(2 * np.pi * y)
x2 = 1.2 * np.sin(3 * np.pi * y)
x2 = np.ma.masked_greater(x2, 1.0)
# plot x1 and plot x2
ax[1].plot(x1, y, color="k", lw=1, ls="-")
ax[1].plot(x2, y, color="k", lw=1, ls="-")
# "where x1 <= x2"
ax[1].fill_betweenx(y, x1, x2, where=x2 >= x1, facecolor="cornflowerblue", alpha=0.7)
# where x1>= x2
ax[1].fill_betweenx(y, x1, x2, where=x2 <= x1, facecolor="darkred", alpha=0.7)
ax[1].set_xlim(-1.2, 1.2)
ax[1].set_ylim(0, 2)
ax[1].grid(ls=":", lw=1, color="gray", alpha=0.5)
plt.tight_layout()
plt.show()
