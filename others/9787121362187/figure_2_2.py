"""
@File         : figure_2_2.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-19 20:20:29
@Email        : cuixuanstephen@gmail.com
@Description  : 椭圆的实现方法
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

fig, ax = plt.subplots(1, 2, subplot_kw={"aspect": "equal"})

angles = np.linspace(0, 135, 4)
# 版本问题：angle 成为关键字参数
# ellipse = [Ellipse((2, 2), 4, 2, a) for a in angles]
ellipse = [Ellipse((2, 2), 4, 2, angle=a) for a in angles]
for elle in ellipse:
    ax[0].add_patch(elle)
    elle.set_alpha(0.4)
    elle.set_color("cornflowerblue")
ax[0].axis([-1, 5, -1, 5])

ellipse = [
    Ellipse(
        xy=np.random.rand(2) * 10,
        width=np.random.rand(1),
        height=np.random.rand(1),
        angle=np.random.rand(1) * 360,
    )
    for _ in range(100)
]
for elle in ellipse:
    ax[1].add_patch(elle)
    elle.set_alpha(np.random.rand())
    elle.set_color(np.random.rand(3))

ax[1].axis([-1, 11, -1, 11])
plt.tight_layout()
plt.show()
