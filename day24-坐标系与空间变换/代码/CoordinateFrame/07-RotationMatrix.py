"""
依次绕着X,Y,Z固定轴旋转变换矩阵
"""
import numpy as np
from numpy import sin, cos

# 保留三位小数，不使用科学技术法
np.set_printoptions(precision=3, suppress=True)

q_x = np.radians(-90)
q_y = np.radians(0)
q_z = np.radians(-90)

R_x = np.array([
    [1, 0, 0],
    [0, cos(q_x), - sin(q_x)],
    [0, sin(q_x),   cos(q_x)],
])

R_y = np.array([
    [cos(q_y), 0, sin(q_y)],
    [0, 1, 0],
    [-sin(q_y), 0, cos(q_y)],
])

R_z = np.array([
    [cos(q_z), - sin(q_z), 0],
    [sin(q_z),   cos(q_z), 0],
    [0, 0, 1],
])

print(R_x)

R = R_z @ R_y @ R_x
print(R)
