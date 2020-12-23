import numpy as np

# 创建向量，世界坐标系->小车坐标系
vec_t = np.array([4, 3])

# 目标在小车坐标系r （robot）下的位置
p_r = np.array([5.5, 4])

# 计算目标在世界坐标系下的位置
p_w = p_r + vec_t

print(p_w)
