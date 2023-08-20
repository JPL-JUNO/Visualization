"""
@Description: 延伸阅读——箱体、箱须、离群值的含义和计算方法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-20 22:03:52
"""

import numpy as np

data = [10, 1, 25, 11, 24, 13, 54, 4, 42, -3]
pc = np.array(data)

Q1 = np.quantile(pc, .25)
Q3 = np.quantile(pc, .75)
median = np.median(pc)
IQR = Q3 - Q1
