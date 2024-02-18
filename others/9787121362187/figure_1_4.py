"""
@File         : figure_1_4.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-18 22:59:08
@Email        : cuixuanstephen@gmail.com
@Description  : 水平方向的交叉曲线的颜色填充方法
"""

# 调用实例方法 fill_between()，通过使用参数 where 的条件表达式参数值，实现满足具体条
# 件的指定区域的颜色填充的目标
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 500)
y1 = np.sin(2 * np.pi * x)
y2 = 1.1 * np.sin(3 * np.pi * x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, lw=1, ls="-")
ax.plot(x, y2, lw=1, ls="-")
ax.fill_between(
    x, y1, y2, where=y2 >= y1, interpolate=True, facecolor="cornflowerblue", alpha=0.7
)
ax.fill_between(
    x, y1, y2, where=y2 < y1, interpolate=True, facecolor="darkred", alpha=0.7
)
ax.set_xlim(0, 2)
ax.set_ylim(-1.2, 1.2)
ax.grid(ls=":", lw=1, color="gray", alpha=0.5)
plt.show()
