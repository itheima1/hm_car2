# p_w : [8.76313972 8.21410162 1. ]  -> p_r


import numpy as np

# 小车坐标系旋转角度
theta = np.radians(30)
# 小车坐标系平移向量
translation = np.array([6, 2])

# 目标在世界坐标系下的位置
p_w = np.array([8.76313972, 8.21410162, 1.0])

# 构建3x3的变换矩阵 (世界->小车)
T = np.array([
    [np.cos(theta), - np.sin(theta), translation[0]],
    [np.sin(theta),   np.cos(theta), translation[1]],
    [0, 0, 1]
])

# 让点 P_w 左乘变换矩阵
p_r = np.linalg.inv(T) @ p_w
print(p_r)

