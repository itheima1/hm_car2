import numpy as np

from transformation import euler2matrix, merge_pose

# 侦察机相对于基地的位置和姿态
p1 = [1.5, 2.8, 3.2]
rpy = np.array([15, 30, 10])

# 目标相对于基地的位置
p2 = np.array([2.286, 5.721, 5.819])

if __name__ == '__main__':
    R1 = euler2matrix(rpy)

    T = merge_pose(R1, p1)

    print(T)

    p2 = np.append(p2, 1.0)

    rst = np.linalg.inv(T) @ p2

    print(rst[:3])

