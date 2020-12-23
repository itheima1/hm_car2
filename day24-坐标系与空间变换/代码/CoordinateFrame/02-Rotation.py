"""
测试坐标系旋转
"""
import numpy as np

# 已知世界坐标系->小车坐标系旋转矩阵
theta = np.deg2rad(30)

R = np.array([
    [np.cos(theta), - np.sin(theta)],
    [np.sin(theta),   np.cos(theta)]
])

# 目标在小车坐标系下的坐标
p_r = np.array([5.5, 4.])

# p_w = R.dot(p_r)
p_w = R @ p_r # @ 作用和.dot一致

print("目标在世界坐标系下的位置：", p_w)
