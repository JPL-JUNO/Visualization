"""
@File         : figure_2_1.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-18 23:14:20
@Email        : cuixuanstephen@gmail.com
@Description  : 圆的实现方法
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

fig, ax = plt.subplots(2, 2)
circle = Circle((2, 2), radius=2)
# 由于坐标轴的刻度线的变化量不一致导致显式的并不是圆
ax[0, 0].add_patch(circle)
ax[0, 0].set_xlim(-1, 5)
ax[0, 0].set_ylim(-1, 5)

rectangle = ax[0, 1].patch
rectangle.set_facecolor("gold")
circle = Circle((2, 2), radius=2, facecolor="white", edgecolor="cornflowerblue")
ax[0, 1].add_patch(circle)
ax[0, 1].set_xlim(-1, 5)
ax[0, 1].set_ylim(-1, 5)
# 实现 x 轴和 y 轴的长度相同、刻度线的变化量相同的目标
ax[0, 1].set_aspect("equal", "box")
rectangle = ax[1, 0].patch
rectangle.set_facecolor("palegreen")
circle = Circle((2, 2), radius=2, facecolor="white", edgecolor="cornflowerblue")
ax[1, 0].add_patch(circle)
# 刻度线的变化量进行调整，使之保持相同的增量，
# 从而产生理想的圆的可视化效果。
ax[1, 0].axis("equal")
rectangle = ax[1, 1].patch
rectangle.set_facecolor("lightskyblue")
circle = Circle((2, 2), radius=2, facecolor="white", edgecolor="cornflowerblue")
ax[1, 1].add_patch(circle)
ax[1, 1].axis([-1, 5, -1, 5])
ax[1, 1].set_yticks(np.arange(-1, 6, 1))
ax[1, 1].axis("equal")
plt.subplots_adjust(left=0.1)
plt.show()
