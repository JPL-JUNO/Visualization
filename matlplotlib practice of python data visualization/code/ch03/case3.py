"""
@Description: 案例——不绘制离群值的水平放置的箱线图
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-20 22:46:57
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"] = ["FangSong"]
plt.rcParams["axes.unicode_minus"] = False
x = np.random.randn(1000)
plt.boxplot(x, vert=False, showfliers=False)
plt.xlabel("随机数值")
plt.yticks([1], ["随机数生成器 AlphaRM"], rotation=90)
plt.title("随机数生成器抗干扰能力的稳定性")
plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=0.4)
plt.show()
