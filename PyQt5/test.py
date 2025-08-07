#import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app = QApplication(sys.argv) #komut satırından alınan argümanlar, komut bilgisini aktarır
    win = QMainWindow()

    win.show()
    sys.exit(app.exec_())

window()