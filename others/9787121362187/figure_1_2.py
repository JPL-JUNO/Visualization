"""
@File         : figure_1_2.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-18 22:48:56
@Email        : cuixuanstephen@gmail.com
@Description  : 不规则多边形的颜色填充
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x)
plt.fill(x, y, color="cornflowerblue", alpha=0.4)
plt.plot(x, y, color="cornflowerblue", alpha=0.8)
plt.plot([x[0], x[-1]], [y[0], y[-1]], color="cornflowerblue", alpha=0.8)
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.1, 1.1)
plt.show()
