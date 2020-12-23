"""
坐标系变换工具
"""
import  numpy as np
from numpy import sin, cos

# 保留三位小数，不使用科学技术法
np.set_printoptions(precision=3, suppress=True, formatter={"float": "{:.3f}".format})

def merge_pose(R, t):
    """
    将传入进来的旋转矩阵，和平移向量合并成一个4x4变换矩阵
    :param R: 3x3 旋转矩阵
    :param t: 3x1 平移矩阵
    :return: pose: 4x4变换矩阵
    """
    mat = np.eye(4, dtype=R.dtype)
    mat[:3, :3] = R
    mat[:3, 3] = t
    return mat

def split_pose(T):
    """
    分解4x4变换矩阵
    :param T: 4x4变换矩阵
    :return: R，t
    """
    return T[:3, :3], T[:3, 3]

if __name__ == '__main__':
    q_x = np.radians(-30)
    q_y = np.radians(10)
    q_z = np.radians(-80)
    R_x = np.array([
        [1, 0, 0],
        [0, cos(q_x), - sin(q_x)],
        [0, sin(q_x), cos(q_x)],
    ])
    R_y = np.array([
        [cos(q_y), 0, sin(q_y)],
        [0, 1, 0],
        [-sin(q_y), 0, cos(q_y)],
    ])
    R_z = np.array([
        [cos(q_z), - sin(q_z), 0],
        [sin(q_z), cos(q_z), 0],
        [0, 0, 1],
    ])

    R = R_z @ R_y @ R_x
    print(R)

    t = np.array([1, 2, 3])
    print(t)
    pose = merge_pose(R, t)
    print("变换矩阵：\n", pose)

    # 4x4矩阵分解成R和t
    R_, t_ = split_pose(pose)
    print(R_)
    print(t_)
