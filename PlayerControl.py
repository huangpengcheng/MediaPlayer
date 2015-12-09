from PyQt5.QtWidgets import (QLabel,QPushButton, QHBoxLayout)


class PlayerControl(QLabel):
    def __init__(self, parent=None):
        super(PlayerControl, self).__init__(parent)
        self.setFixedHeight(25)

        self.pbn_Player = QPushButton(self)
        self.pbn_PlayNext = QPushButton(self)
        self.pbn_PlayPrevious = QPushButton(self)
        self.pbn_PlayVolume = QPushButton(self)
        self.pbn_Player.setFixedSize(25, 25)
        self.pbn_PlayNext.setFixedSize(25, 25)
        self.pbn_PlayVolume.setFixedSize(25, 25)
        self.pbn_PlayPrevious.setFixedSize(25, 25)

        self.layout_bottom = QHBoxLayout(self)
        self.layout_bottom.addWidget(self.pbn_Player)
        self.layout_bottom.addWidget(self.pbn_PlayNext)
        self.layout_bottom.addWidget(self.pbn_PlayPrevious)
        self.layout_bottom.addWidget(self.pbn_PlayVolume)
        self.layout_bottom.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_bottom)
