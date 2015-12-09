# coding: utf-8
from PyQt5.QtCore import (Qt, QPoint)
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QGridLayout)
import WindowTools
import PlayerArea
import PlayerControl


class MyMusicMedia(QWidget):
    def __init__(self, parent=None):
        super(MyMusicMedia, self).__init__(parent)
        self.__offset = QPoint(0, 0)
        self.resize(750, 480)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)
        self.background = QLabel()

        self.lab_top = WindowTools()        # 顶部按钮声明
        self.lab_middle = PlayerArea()      # 中间部件声明
        self.lab_bottom = PlayerControl()   # 底部部件声明

        self.layout_vertical = QVBoxLayout()
        self.layoutTop = QGridLayout()

        self.set_widgets()

    def set_widgets(self):
        # 垂直布局
        self.layout_vertical.addWidget(self.lab_top)
        self.layout_vertical.addWidget(self.lab_middle)
        self.layout_vertical.addWidget(self.lab_bottom)
        self.background.setLayout(self.layout_vertical)

        self.layoutTop.setContentsMargins(0, 0, 0, 0)
        self.layoutTop.addWidget(self.background)
        self.setLayout(self.layoutTop)

        # 设置样式表
        self.background.setObjectName("background")
        self.CloseWindow.setObjectName('CloseWindow')
        self.MinWindow.setObjectName('MinWindow')
        self.setStyleSheet(
            "#background{"
            "border-image:url(Images/background.png);"
            "}"
            "#CloseWindow{"
            "background:red;"
            "}"
            "#MinWindow{"
            "background:blue;"
            "}"
            )

# 鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__offset = event.globalPos() - self.pos()  # 获得鼠标位置和窗口的坐标差

# 鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.__offset)    # 移动到该出现的位置

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = MyMusicMedia()
    widget.show()
    sys.exit(app.exec_())
