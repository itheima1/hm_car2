# pid控制器 案例
from robot import Robot, show


def run(robot, n=100, speed=1.0):
    """
    运行多次运动并记录轨迹
    :param robot:   小车
    :param n:       循环次数
    :param speed:   小车速度
    """
    x_trajectory = []
    y_trajectory = []
    for i in range(n):
        # ---------------------------- start

        steer = 0.0

        # ---------------------------- end
        # 以steer为偏转角，speed为速度，执行一次运动
        robot.move(steer, speed)
        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)
        print(robot)
    return x_trajectory, y_trajectory


if __name__ == '__main__':
    # 创建
    robot = Robot()
    # 初始位置 x=0, y=-1, orient=0
    robot.set(0, -1, 0)

    # 运行并收集所有的x，y
    x_trajectory, y_trajectory = run(robot)

    # 可视化运行结果
    show(x_trajectory, y_trajectory, label='Car')