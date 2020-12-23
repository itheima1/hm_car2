"""
三维坐标系下的平移
"""
import numpy as np

# 无人机的坐标
vec_t = np.array([1, 2, 2.5])

# 目标点在无人机坐标系下位置
p_r =np.array([0, 3, 2])

# 求：目标点在世界坐标系下位置
print(vec_t + p_r)
