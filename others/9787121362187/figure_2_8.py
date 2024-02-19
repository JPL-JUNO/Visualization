"""
@File         : figure_2_8.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-19 22:40:59
@Email        : cuixuanstephen@gmail.com
@Description  : 使用楔形绘制圆环式饼图
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Rectangle

fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
font_style = {"family": "serif", "size": 12, "style": "italic", "weight": "black"}
sample_data = [350, 150, 200, 300]
total = sum(sample_data)
percents = [i / float(total) for i in sample_data]
angles = [360 * i for i in percents]
delta = 45
wedge1 = Wedge((2, 1.9), 1, delta, delta + sum(angles[0:1]), color="orange", width=0.3)
wedge2 = Wedge(
    (2, 1.9),
    1,
    delta + sum(angles[0:1]),
    delta + sum(angles[0:2]),
    facecolor="steelblue",
    edgecolor="white",
    width=0.3,
)
wedge3 = Wedge(
    (2, 1.9),
    1,
    delta + sum(angles[0:2]),
    delta + sum(angles[0:3]),
    facecolor="darkred",
    edgecolor="white",
    width=0.3,
)
wedge4 = Wedge(
    (2, 1.9),
    1,
    delta + sum(angles[0:3]),
    delta,
    facecolor="lightgreen",
    edgecolor="white",
    width=0.3,
)


colors = ["steelblue", "darkred", "lightgreen"]
rectangle1 = Rectangle((3.2, 0.1), 0.3, 0.2, color="orange")
rectangle2 = Rectangle((3.2, 0.4), 0.3, 0.2, color="steelblue")
rectangle3 = Rectangle((3.2, 0.7), 0.3, 0.2, color="darkred")
rectangle4 = Rectangle((3.2, 1.0), 0.3, 0.2, color="lightgreen")
wedges = [
    wedge1,
    wedge2,
    wedge3,
    wedge4,
    rectangle1,
    rectangle2,
    rectangle3,
    rectangle4,
]
for wedge in wedges:
    ax.add_patch(wedge)
ax.text(3.6, 0.1, f"{percents[0]*100:3.1f}%", **font_style)
ax.text(3.6, 0.4, f"{percents[1]*100:3.1f}%", **font_style)
ax.text(3.6, 0.7, f"{percents[2]*100:3.1f}%", **font_style)
ax.text(3.6, 1.0, f"{percents[3]*100:3.1f}%", **font_style)
ax.axis([0, 4.5, -0.5, 4])
plt.show()
