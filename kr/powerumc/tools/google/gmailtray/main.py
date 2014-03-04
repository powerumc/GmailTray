# coding: utf-8

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_MainWindow import Ui_MainWindow
from GmailWindow import GmailWindow




if __name__ == '__main__':

    
#     if QSystemTrayIcon.isSystemTrayAvailable() == False:
#         QMessageBox.critical(0, "Systray", "I couldn't detect any system tray on this system.")
#         sys.exit()

    app = QApplication(sys.argv)

    w = GmailWindow()
    w.show()


    
    sys.exit(app.exec_())