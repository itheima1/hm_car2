"""
pid控制器 pid-控制器案例
"""
from robot import Robot, show
import numpy as np


def run(robot, k_p, k_d, k_i, n=100, speed=1.0):
    """
    运行多次运动并记录轨迹
    :param robot:   小车
    :param k_p:     p增益Gain系数
    :param k_d:     d增益Gain系数
    :param k_i:     i增益Gain系数
    :param n:       循环次数
    :param speed:   小车速度
    """
    x_trajectory = []
    y_trajectory = []
    p_arr = []
    d_arr = []
    i_arr = []
    prev_cte = robot.y # 上一次的cte
    cte_sum = 0
    for i in range(n):
        # ---------------------------- start
        cte = 0.0 - robot.y # 误差值
        p = k_p * cte                    # p

        d = k_d * (cte - prev_cte) / 1.0 # d
        prev_cte = cte

        cte_sum += cte
        i = k_i * cte_sum                # i

        steer = p + d + i

        p_arr.append(p)
        d_arr.append(d)
        i_arr.append(i)
        # ---------------------------- end
        # 以steer为偏转角，speed 为速度，执行一次运动
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        print(robot)
    return x_trajectory, y_trajectory, p_arr, d_arr, i_arr


if __name__ == '__main__':
    # 创建
    robot = Robot()
    # 初始位置 x=0, y=-1, orient=0
    robot.set(0, -1, 0)
    # 设置10度的轮子系统性偏差
    robot.set_steering_drift(10. / 180. * np.pi)

    # 运行并收集所有的x，y
    x_trajectory, y_trajectory, p_arr, d_arr, i_arr = run(robot, k_p=0.2, k_d=3.0, k_i=0.005)
    # 可视化运行结果
    show(x_trajectory, y_trajectory, p_array=p_arr, d_array=d_arr, i_array=i_arr, label='PID')

    k_p, k_d, k_i = [10.716018504541431, 18.68325573584582, 0.020275559590445292]
    robot.reset()
    # 运行并收集所有的x，y
    x_trajectory, y_trajectory, p_arr, d_arr, i_arr = run(robot, k_p=k_p, k_d=k_d, k_i=k_i)
    # 可视化运行结果
    show(x_trajectory, y_trajectory, p_array=p_arr, d_array=d_arr, i_array=i_arr, label='PID')

