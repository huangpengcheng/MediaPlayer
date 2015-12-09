# coding: utf_8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication


class MyMusicMedia(QWidget):
    def __init__(self, parent=None):
        super(MyMusicMedia, self).__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyMusicMedia()
    widget.show()
    sys.exit(app.exec_())