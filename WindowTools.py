from PyQt5.QtWidgets import (QApplication, QLabel, QToolButton, QHBoxLayout)


class WindowTools(QLabel):
    def __init__(self, parent=None):
        super(WindowTools, self).__init__(parent)
        self.setFixedHeight(25)

        self.CloseWindow = QToolButton(self)
        self.MinWindow = QToolButton(self)
        self.CloseWindow.setFixedSize(12, 12)
        self.MinWindow.setFixedSize(12, 12)

        self.layout_top = QHBoxLayout(self)
        self.layout_top.addStretch()
        self.layout_top.addWidget(self.MinWindow)
        self.layout_top.addWidget(self.CloseWindow)
        self.setLayout(self.layout_top)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    test = WindowTools()
    test.show()
    sys.exit(app.exec_())
