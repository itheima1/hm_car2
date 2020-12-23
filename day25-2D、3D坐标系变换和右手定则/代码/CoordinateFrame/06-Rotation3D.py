"""
三维坐标系旋转变换 - 绕Z变换
"""
import numpy as np

np.set_printoptions(precision=3, formatter={"float": "{:.3f}".format})

# print("float: {:.3f}".format(2.123456))
# print("float: {:.3f}".format(3.))

# 世界坐标系 -> 小车坐标系
theta = np.radians(30)

R = np.array([
    [np.cos(theta), - np.sin(theta), 0],
    [np.sin(theta),   np.cos(theta), 0],
    [0, 0, 1],
])

# 假如已知目标在无人机坐标系位置
p_r = np.array([5.5, 4.0, 3.0])

p_w = R @ p_r

print(p_w)
