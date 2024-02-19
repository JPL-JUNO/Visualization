"""
@File         : figure_2_7.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-19 22:26:18
@Email        : cuixuanstephen@gmail.com
@Description  : 使用楔形绘制饼图
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
font_style = {"family": "serif", "size": 12, "style": "italic", "weight": "black"}
sample_data = [350, 150, 200, 300]
total = sum(sample_data)
percents = [i / float(total) for i in sample_data]
angles = [360 * i for i in percents]
delta = 45
wedge1 = Wedge((2, 2), 1, delta, delta + sum(angles[0:1]), color="orange")
wedge2 = Wedge(
    (2, 1.9),
    1,
    delta + sum(angles[0:1]),
    delta + sum(angles[0:2]),
    facecolor="steelblue",
    edgecolor="white",
)
wedge3 = Wedge(
    (2, 1.9),
    1,
    delta + sum(angles[0:2]),
    delta + sum(angles[0:3]),
    facecolor="darkred",
    edgecolor="white",
)
wedge4 = Wedge(
    (2, 1.9),
    1,
    delta + sum(angles[0:3]),
    delta,
    facecolor="lightgreen",
    edgecolor="white",
)

wedges = [wedge1, wedge2, wedge3, wedge4]
colors = ["steelblue", "darkred", "lightgreen"]
# for wedge in [
#     Wedge(
#         (2, 1.9), 1, delta + sum(angles[0:i]), delta, facecolor=color, edgecolor="white"
#     )
#     for i, color in enumerate(np.random.rand(4, 3), start=1)
# ]:
for wedge in wedges:
    ax.add_patch(wedge)
ax.text(1.7, 2.5, f"{percents[0]*100:3.1f}%", **font_style)
ax.text(1.2, 1.7, f"{percents[1]*100:3.1f}%", **font_style)
ax.text(1.7, 1.2, f"{percents[2]*100:3.1f}%", **font_style)
ax.text(2.5, 1.7, f"{percents[3]*100:3.1f}%", **font_style)
ax.axis([0, 4, 0, 4])
plt.show()
