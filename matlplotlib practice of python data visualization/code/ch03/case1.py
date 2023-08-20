"""
@Description: 案例——绘制内嵌环形饼图
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-20 15:51:44
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

elements = ["面粉", "砂糖", "奶油", "草莓酱", "坚果"]
weight1 = [40, 15, 20, 10, 15]
weight2 = [30, 25, 15, 20, 10]
colormapList = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

wedges1, texts1, autotexts1 = plt.pie(weight1,
                                      autopct="%3.1f%%",
                                      radius=1,
                                      pctdistance=.8,
                                      colors=colormapList,
                                      textprops=dict(color='w'),
                                      wedgeprops=dict(width=.3, edgecolor='w'))
wedges2, texts2, autotexts2 = plt.pie(weight2,
                                      autopct="%3.1f%%",
                                      radius=0.7,
                                      pctdistance=0.75,
                                      colors=colormapList,
                                      textprops=dict(color="w"),
                                      wedgeprops=dict(width=0.3, edgecolor="w"))
plt.legend(wedges1,
           elements,
           fontsize=12,
           title="配料表",
           loc="center left",
           bbox_to_anchor=(0.91, 0, 0.3, 1))
plt.setp(autotexts1, size=10, weight="bold")
plt.setp(autotexts2, size=10, weight="bold")
plt.setp(texts1, size=12)
plt.title("不同果酱面包配料比例表的比较")
plt.savefig('code/ch03/绘制内嵌环形饼图.png', dpi=300)
plt.show()
