"""
把旋转矩阵和平移向量结合成一个3x3变换矩阵
2D
"""
import numpy as np

# 小车坐标系旋转角度
theta = np.radians(30)
# 小车坐标系平移向量
translation = np.array([6, 2])
# 目标在小车坐标系下的位置
p_r = np.array([5.5, 4.0, 1.0])

# 构建3x3的变换矩阵
T = np.array([
    [np.cos(theta), - np.sin(theta), translation[0]],
    [np.sin(theta),   np.cos(theta), translation[1]],
    [0, 0, 1]
])

# 让点 P_r 左乘变换矩阵
p_w = T @ p_r
print(p_w)

