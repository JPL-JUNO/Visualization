"""
@Description: 函数的组合应用
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-15 20:01:06
"""
import matplotlib.pyplot as plt
import numpy as np

NUMS = 100
x = np.linspace(.5, 3.5, NUMS)
y = np.sin(x)
y1 = np.random.randn(NUMS)

# 绘制散点图
plt.scatter(x, y1, c='.25', label='scatter figure')

# 绘制折线图
plt.plot(x, y, ls='--', lw=2, label='plot figure')

plt.xlim(0.0, 4.0)
plt.ylim(-3.0, 3.0)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.grid(True, ls=':', color='r')

# 增加垂直区域
plt.axvspan(xmin=1.0, xmax=2.0, facecolor='y', alpha=.3)
# 增加水平线
plt.axhline(y=0.0, c='r', ls='--', lw=2)

plt.annotate('maximum',
             xy=(np.pi / 2, 1.0),
             xytext=(np.pi / 2 + .15, 1.5),
             weight='bold',
             color='r',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'))
plt.annotate('spines',
             xy=(.75, -3),
             xytext=(.35, -2.25),
             weight='bold',
             color='b',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.annotate("",
             xy=(3.5, -2.98),
             xytext=(3.6, -2.70),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.annotate("",
             xy=(0, -2.78),
             xytext=(.4, -2.32),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.text(3.6, -2.7, "'|' is tickline", weight='bold', color='b')
plt.text(3.6, -2.95, "'3.5' is ticklabel", weight='bold', color='b')
plt.title('structure of matplotlib')
plt.legend()

for spine in plt.gca().spines.keys():
    if spine in ('top', 'right'):
        plt.gca().spines[spine].set_color('none')
plt.gca().xaxis.set_ticks_position('bottom')
# leave left ticks for y-axis on
# set tick_line position of left
plt.gca().yaxis.set_ticks_position('left')
# 获取当前画布， 更改其大小
plt.gcf().set_size_inches(12, 8)
plt.savefig('code/structure of matplotlib.png', dpi=300)
plt.show()
