from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtMultimedia
import sys
from interface import Ui_PianoForte

from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class PianoForte(QWidget, Ui_PianoForte):
    def __init__(self):
        super(PianoForte, self).__init__()
        self.notes = ["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B"]
        self.max_players = 10
        self.initUI()
        self.init_players()

    def initUI(self):
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.Cbutton.note = "C"
        self.Cbutton.clicked.connect(self.play)
        self.Csbutton.note = "Cs"
        self.Csbutton.clicked.connect(self.play)
        self.Dbutton.note = "D"
        self.Dbutton.clicked.connect(self.play)
        self.Dsbutton.note = "Ds"
        self.Dsbutton.clicked.connect(self.play)
        self.Ebutton.note = "E"
        self.Ebutton.clicked.connect(self.play)
        self.Fbutton.note = "F"
        self.Fbutton.clicked.connect(self.play)
        self.Fsbutton.note = "Fs"
        self.Fsbutton.clicked.connect(self.play)
        self.Gbutton.note = "G"
        self.Gbutton.clicked.connect(self.play)
        self.Gsbutton.note = "Gs"
        self.Gsbutton.clicked.connect(self.play)
        self.Abutton.note = "A"
        self.Abutton.clicked.connect(self.play)
        self.Asbutton.note = "As"
        self.Asbutton.clicked.connect(self.play)
        self.Bbutton.note = "B"
        self.Bbutton.clicked.connect(self.play)

    def init_players(self):
        self.players = list()

    def play(self):
        note = self.sender().note
        media = QtCore.QUrl.fromLocalFile(f"\\Users\\mares\\PycharmProjects\\PianoForte\\res\\guitar\\{note}.mp3")
        content = QtMultimedia.QMediaContent(media)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        self.players.append(player)
        while len(self.players) > self.max_players:
            self.players.pop(0)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_A:
            self.Cbutton.click()
        if event.key() == Qt.Key_W:
            self.Csbutton.click()
        if event.key() == Qt.Key_S:
            self.Dbutton.click()
        if event.key() == Qt.Key_E:
            self.Dsbutton.click()
        if event.key() == Qt.Key_D:
            self.Ebutton.click()
        if event.key() == Qt.Key_F:
            self.Fbutton.click()
        if event.key() == Qt.Key_T:
            self.Fsbutton.click()
        if event.key() == Qt.Key_G:
            self.Gbutton.click()
        if event.key() == Qt.Key_Y:
            self.Gsbutton.click()
        if event.key() == Qt.Key_H:
            self.Abutton.click()
        if event.key() == Qt.Key_U:
            self.Asbutton.click()
        if event.key() == Qt.Key_J:
            self.Bbutton.click()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = PianoForte()
    wid.show()
    sys.exit(app.exec())
