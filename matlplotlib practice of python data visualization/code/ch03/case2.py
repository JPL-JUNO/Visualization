"""
@Description: 案例——水平方向的箱线图
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-20 22:30:55
"""

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
import numpy as np

x = np.random.randn(1_000)
plt.boxplot(x,
            vert=False,
            sym='+',
            color='b'
            )
plt.xlabel("随机数值")
plt.yticks([1], ["随机数生成器 AlphaRM"], rotation=90)
plt.title("随机数生成器抗干扰能力的稳定性")
plt.grid(axis="x", ls=":", lw=1, color="gray", alpha=0.4)
plt.show()
