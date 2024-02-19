"""
@File         : figure_2_5.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-19 21:52:48
@Email        : cuixuanstephen@gmail.com
@Description  : 使用折线绘制圆
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

fig, ax = plt.subplots(2, 2)
x = np.linspace(0, 2 * np.pi, 500)
y1 = 2 * np.cos(x)
y2 = 2 * np.sin(x)

ax[0, 0].plot(y1, y2, color="cornflowerblue", lw=2)
ax[0, 0].set_xlim(-3, 3)
ax[0, 0].set_ylim(-3, 3)

rectangle = ax[0, 1].patch
rectangle.set_facecolor("gold")
ax[0, 1].plot(y1, y2, color="cornflowerblue", lw=2)
ax[0, 1].set_xlim(-3, 3)
ax[0, 1].set_ylim(-3, 3)
ax[0, 1].set_aspect("equal", "box")

rectangle = ax[1, 0].patch
rectangle.set_facecolor("palegreen")
ax[1, 0].plot(y1, y2, color="cornflowerblue", lw=2)
ax[1, 0].axis("equal")

rectangle = ax[1, 1].patch
rectangle.set_facecolor("lightskyblue")
ax[1, 1].plot(y1, y2, color="cornflowerblue", lw=2)
ax[1, 1].axis([-3, 3, -3, 3])
# 这条代码没有任何用处
ax[1, 1].set_yticks(np.arange(-3, 4, 1))
ax[1, 1].axis("equal")
plt.subplots_adjust(left=0.1)
plt.show()
# 调用实例方法 plot()绘制的圆和调用类 Circle 绘制的圆在展示效果上有所区别。调用实例方法
# plot()绘制的圆没有覆盖坐标轴的绘图区域；而调用类 Circle 绘制的圆即使在填充颜色是白色的情况
# 下，也会覆盖坐标轴的绘图区域。
