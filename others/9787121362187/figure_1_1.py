"""
@File         : figure_1_1.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-18 22:49:05
@Email        : cuixuanstephen@gmail.com
@Description  : 规则多边形的颜色填充
"""

import matplotlib.pyplot as plt
import numpy as np

x = [0, 0, 5, 10, 15, 15, 10, 5]
y = [5, 10, 15, 15, 10, 5, 0, 0]
# 通过调用函数 fill()来完成绘制
plt.fill(x, y, color="cornflowerblue")
plt.xlim(-1, 16)
plt.ylim(-1, 16)
plt.xticks(np.arange(0, 16, 5))
plt.yticks(np.arange(0, 16, 5))
plt.show()
