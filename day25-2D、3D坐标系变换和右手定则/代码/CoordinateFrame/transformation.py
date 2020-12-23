"""
坐标系变换工具
"""
import numpy as np
from math import sin, cos, atan2

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


def euler2matrix(theta, format="degree"):
    if format == "degree":
        # 将角度值转成弧度  theta = theta / 180.0 * np.pi
        theta = np.deg2rad(theta)

    q_x, q_y, q_z = theta

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

    return R_z @ R_y @ R_x

def is_rotation_matrix(R):
    """
    确认其是一个旋转矩阵
    """
    # 求R的转置
    Rt = np.transpose(R)
    # 矩阵 @ 自己的逆 == 单位矩阵
    should_be_identity = R @ Rt
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - should_be_identity)
    return n < 1e-6

def matrix2euler(R):
    """
    旋转矩阵转欧拉角(zyx),  RPY
    :param R: 旋转矩阵
    :return: 欧拉角(zyx)的x，y，z
    """
    # 旋转矩阵：正交矩阵 （转置==逆） （矩阵 @ 矩阵的逆 == I单位矩阵）
    assert (is_rotation_matrix(R)) # 断言结果

    sy = np.sqrt(R[0, 0] ** 2 + R[1, 0] ** 2)

    # 判断是否是奇异矩阵
    singular = sy < 1e-6

    if not singular:
        z = atan2(R[1, 0], R[0, 0])
        y = atan2(-R[2, 0], sy)
        x = atan2(R[2, 1], R[2, 2])
    else:
        z = 0
        y = atan2(-R[2, 0], sy)
        x = -atan2(R[1, 2], R[1, 1])

    return np.array([x, y, z])


if __name__ == '__main__':
    # 输入参数，x，y，z角度
    R = euler2matrix((60, 80, -24))
    # 输出结果，旋转矩阵
    print(R)

    # 旋转矩阵转回欧拉角
    theta = matrix2euler(R)
    print(np.rad2deg(theta))

    # t = np.array([1, 2, 3])
    # print(t)
    # pose = merge_pose(R, t)
    # print("变换矩阵：\n", pose)
    #
    # # 4x4矩阵分解成R和t
    # R_, t_ = split_pose(pose)
    # print(R_)
    # print(t_)
