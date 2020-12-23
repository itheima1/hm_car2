import random
import numpy as np
import matplotlib.pyplot as plt

class Robot(object):

    def __init__(self, length=20.0):
        """
        创建机器人并初始化位置和方向为0, 0, 0.
        """
        self.x = 0.0
        self.y = 0.0
        self.orientation = 0.0    # 与X轴正方向的夹角（单位为弧度）
        self.length = length      # 前后轮子的轴距
        self.steering_noise = 0.0 # 方向噪声
        self.distance_noise = 0.0 # 距离噪声
        self.steering_drift = 0.0 # 方向漂移

        self.default_state = {"x": self.x,"y": self.y,"o": self.orientation}

    def reset(self):
        self.x = self.default_state["x"]
        self.y = self.default_state["y"]
        self.orientation = self.default_state["o"]

    def set(self, x, y, orientation):
        """
        设置机器人的坐标及方向
        """
        self.x = x
        self.y = y
        self.orientation = orientation % (2.0 * np.pi)
        self.default_state = {"x": self.x,"y": self.y,"o": self.orientation}

    def set_noise(self, steering_noise, distance_noise):
        """
        设置噪声参数
        :param steering_noise: 转向噪声
        :param distance_noise: 距离噪声
        """
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.steering_noise = steering_noise
        self.distance_noise = distance_noise

    def set_steering_drift(self, drift):
        """
        设置系统的转向漂移参数
        """
        self.steering_drift = drift

    def move(self, steering, distance, tolerance=0.001, max_steering_angle=np.pi / 4.0):
        """
        小车的移动函数

        :param steering: 前轮的转向角，最大值为max_steering_angle
        :param distance: 总行驶距离，一般为非负
        :param tolerance: 转向的最小差值（阈值），小于此阈值时，让小车走直线，单位为弧度
        :param max_steering_angle: 最大转向角，默认为 180 / 4.0 = 45°
        """
        # if steering > max_steering_angle:
        #     steering = max_steering_angle
        # if steering < -max_steering_angle:
        #     steering = -max_steering_angle
        steering = np.clip(steering, -max_steering_angle, max_steering_angle)
        if distance < 0.0:
            distance = 0.0

        # apply noise
        steering2 = random.gauss(steering, self.steering_noise)
        distance2 = random.gauss(distance, self.distance_noise)

        # apply steering drift
        steering2 += self.steering_drift

        # 角速度 = 线速度 / 转弯半径
        # Execute motion
        turn = np.tan(steering2) * distance2 / self.length

        if abs(turn) < tolerance:
            # approximate by straight line motion 近似直线模型
            self.x += distance2 * np.cos(self.orientation)
            self.y += distance2 * np.sin(self.orientation)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
        else:
            # approximate bicycle model for motion 近似自行车模型
            radius = distance2 / turn
            cx = self.x - (np.sin(self.orientation) * radius)
            cy = self.y + (np.cos(self.orientation) * radius)
            self.orientation = (self.orientation + turn) % (2.0 * np.pi)
            self.x = cx + (np.sin(self.orientation) * radius)
            self.y = cy - (np.cos(self.orientation) * radius)

    def __repr__(self):
        return '[x=%.5f y=%.5f orient=%.5f]' % (self.x, self.y, self.orientation)


def show(x_trajectory, y_trajectory, p_array=[], i_array=[], d_array=[], label = 'PID'):
    n = len(x_trajectory)
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
    # fig, ax1 = plt.subplots(figsize=(8, 4))
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(x_trajectory, np.zeros(n), 'pink', label='reference')
    ax1.plot(x_trajectory, y_trajectory, 'black', label= label + ' controller')
    ax1.set_xlabel('x')  # Add an x-label to the axes.
    ax1.set_ylabel('y')  # Add a y-label to the axes.
    ax1.set_title('Car-Position')
    h, l = ax1.get_legend_handles_labels()
    ax1.legend(h, l)  # h 为线条对象列表， l为文字描述列表

    ax2 = fig.add_subplot(212)
    if len(p_array) > 0:
        ax2.plot(x_trajectory, p_array, color='r', label='p')
    if len(i_array) > 0:
        ax2.plot(x_trajectory, i_array, color='g', label='i')
    if len(d_array) > 0:
        ax2.plot(x_trajectory, d_array, color='b', label='d')

    ax2.set_title('PID-Value')
    h, l = ax2.get_legend_handles_labels()
    ax2.legend(h, l)  # h 为线条对象列表， l为文字描述列表

    plt.ylim((-0.5, 0.5))
    plt.tight_layout()
    plt.show()