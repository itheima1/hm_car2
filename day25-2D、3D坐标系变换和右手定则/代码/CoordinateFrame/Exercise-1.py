"""
已知

- 一个侦察机相对于总部的位置 $P_1 = {^B}P_Q = [1.5, 2.8, 3.2]$
- 侦察机其姿态 $RPY = [15, 30, 10]$ 单位为角度

求其位姿 $T_1 = {^B_Q}T$ ？

- 若已知目标相对于侦察机的位置为 $P_2 = {^Q}P_E = [-0.2, 3.4, 2.1]$，

求敌军目标相对于基地的坐标位置 ${^B}P_E$ ？
"""
import numpy as np
from transformation import *

# 声明侦察机相对于基地的位置和姿态
p1 = np.array([1.5, 2.8, 3.2])
rpy = np.array([15, 30, 10])
# rpy = np.array([0, 0, 0])

# 目标相对于侦察机位置
p2 = np.array([-0.2, 3.4, 2.1])


if __name__ == '__main__':
    # 求目标相对于基地位置p3
    # 1. 构建侦察机的位姿T
    R1 = euler2matrix(rpy)
    T = merge_pose(R1, p1)
    print(T)

    # 为了齐次
    p2 = np.append(p2, 1.0)

    # 2. 通过p3 = T @ p2 得到结果
    p3 = np.dot(T, p2)

    print(p3[:3])