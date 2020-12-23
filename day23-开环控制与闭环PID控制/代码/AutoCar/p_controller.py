# pid控制器 p-控制器案例
from robot import Robot, show


def run(robot, k_p, n=100, speed=1.0):
    """
    运行多次运动并记录轨迹
    :param robot:   小车
    :param k_p:     p增益Gain系数
    :param n:       循环次数
    :param speed:   小车速度
    """
    x_trajectory = []
    y_trajectory = []
    p_arr = []
    for i in range(n):
        # ---------------------------- start
        cte = 0.0 - robot.y # 误差值
        p = k_p * cte       # p

        steer = p

        p_arr.append(p)
        # ---------------------------- end
        # 以steer为偏转角，speed 为速度，执行一次运动
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        print(robot)
    return x_trajectory, y_trajectory, p_arr


if __name__ == '__main__':
    # 创建
    robot = Robot()
    # 初始位置 x=0, y=-1, orient=0
    robot.set(0, -1, 0)

    # 运行并收集所有的x，y
    x_trajectory, y_trajectory, p_arr = run(robot, k_p = 0.2)
    # 可视化运行结果
    show(x_trajectory, y_trajectory, p_array=p_arr, label='P')