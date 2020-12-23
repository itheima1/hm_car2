"""
PID参数调优

twiddle 技术让计算机帮我们调整参数，根据误差均值，调优参数
"""

from robot import Robot, show
import math


def make_robot():
    robot = Robot()
    # 设置位置 （0， -1）, 初始小车方向 0
    robot.set(0, -1, 0)
    # 设置的小车漂移（系统性偏差）
    # robot.set_steering_drift(math.radians(10.))

    return robot

def run(robot, params, n = 100, speed = 1.0):
    """
    运行机器人
    :param robot: 将要运行小车对象
    :param params: 包含k_p, k_d, k_i的参数列表
    """
    x_trajectory = []
    y_trajectory = []

    # 记录总误差
    err = 0

    k_p, k_d, k_i = params
    prev_cte = 0 - robot.y # 上一次的误差
    cte_sum = 0 # 累计误差
    for i in range( 2 * n ):
        cte = 0 - robot.y
        diff_cte = cte - prev_cte
        prev_cte = cte
        cte_sum += cte

        steer = k_p * cte + k_d * diff_cte + k_i * cte_sum

        robot.move(steer, speed)

        x_trajectory.append(robot.x)
        y_trajectory.append(robot.y)

        if i >= n:
            # 从全程的一半开始，到最后误差
            err += cte ** 2

    return x_trajectory, y_trajectory, err / n


def twiddle(tol = 0.08):
    """
    :param tolerance 变化系数最小阈值
    :return: params 包含了 k_p, k_d, k_i 参数列表
    """
    k_pid = [0, 0, 0]  # 初始的k_p值
    dp = 1.0  # 初始的参数变化系数

    robot = make_robot()

    # 运行一次机器人，得到初始的误差均值
    x_trajectory, y_trajectory, best_err = run(robot, k_pid)

    it = 0
    # 利用循环，不断的修改 k_p 值，修改幅度由 dp 决定
    while dp > tol:
        # 循环，直到 k_p 变化幅度 dp 小于 tol 阈值
        k_pid[0] += dp

        # 运行一次机器人，得到更新后的误差均值
        robot.reset()
        x_trajectory, y_trajectory, err = run(robot, k_pid)
        if err < best_err:
            # 在此方向有利于减少误差均值
            best_err = err
            # 把刚刚的增益系数变化量扩大
            dp *= 1.1
        else:
            # 在此方向上不利于减少误差均值，把刚加的值去掉，还要往反方向减一倍
            k_pid[0] -= 2 * dp

            robot.reset()
            x_trajectory, y_trajectory, err = run(robot, k_pid)

            if err < best_err:
                # 在此方向有利于减少误差均值
                best_err = err
                dp *= 1.1
            else:
                k_pid[0] += dp # 把k值恢复原始值
                dp *= 0.9      # 缩小增益系数变换量

        it += 1

        print("Iteration: {}, best_err: {} dp: {}".format(it, best_err, dp))

    return k_pid, best_err



if __name__ == '__main__':
    params, err = twiddle()

    print("Final twiddle error: {} params: {}".format(err, params))

    robot = make_robot()
    x_trajectory, y_trajectory, best_err = run(robot, params)
    show(x_trajectory, y_trajectory, label="Twiddle PID")

