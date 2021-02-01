"""
Created by Kaijun on 2021/2/1
"""
from stm32driver import ZxcarDriver
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QVBoxLayout
import sys

if __name__ == '__main__':
    # 1.创建应用程序
    app = QApplication(sys.argv)
    # 2. 创建窗口
    w = QWidget()
    w.setWindowTitle("测试小车")

    vbox = QVBoxLayout()

    driver = ZxcarDriver("COM25");

    start = QPushButton()
    start.setText("开始")
    vbox.addWidget(start);
    start.clicked.connect(lambda : driver.send_vel(0.5,0))

    stop = QPushButton()
    stop.setText("停止")
    vbox.addWidget(stop);
    stop.clicked.connect(lambda: driver.send_vel(0, 0))

    w.setLayout(vbox)
    w.show()

    sys.exit(app.exec());