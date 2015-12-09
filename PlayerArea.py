from PyQt5.QtWidgets import (QLabel, QTreeWidget, QHBoxLayout)


class PlayerArea(QLabel):
    def __init__(self, parent=None):
        super(PlayerArea, self).__init__(parent)

        self.tree_SongList = QTreeWidget(self)
        self.lab_LyricList = QLabel(self)

        self.layout_middle = QHBoxLayout(self)
        self.layout_middle.addWidget(self.tree_SongList, 2)
        self.layout_middle.addWidget(self.lab_LyricList, 4)
        self.setLayout(self.layout_middle)
