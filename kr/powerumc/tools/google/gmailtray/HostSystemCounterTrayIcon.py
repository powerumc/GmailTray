# coding: utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class HostSystemCounterTrayIcon(QSystemTrayIcon):

    def __init__(self, trayimage):
        QSystemTrayIcon.__init__(self)
        
        if( trayimage is QImage): self.trayiamge = trayimage
        
        

    def __onChangeCount(self, count):
        iconRect = QRect(0,0,20,20)
        _textRect = iconRect.width() / 2.5
        _textRect = QRect(_textRect, _textRect, iconRect.size().width() - _textRect,
                                                iconRect.size().height() - _textRect)
        
        pixmap = QPixmap(iconRect.width(), iconRect.height())
        painter = QPainter(pixmap)
        painter.drawPixel(iconRect, pixmap)
        
        if self.trayiamge != None: 
            painter.drawImage(iconRect, self.trayiamge)

        if count != 0:
            # 숫자 이미지 그림
            painter.setFont(QFont('Arial', 12))
            painter.fillRect(_textRect, Qt.red)
            painter.setPen(Qt.white)
            painter.drawText(_textRect, count, QTextOption(Qt.AlignCenter))
        
        icon = QIcon(pixmap)

        self.icon().detach()
        self.setIcon(icon)
        
        
        