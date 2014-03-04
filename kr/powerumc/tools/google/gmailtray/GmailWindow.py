# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtWebKit import *
from Ui_MainWindow import Ui_MainWindow
from HostSystemCounterTrayIcon import HostSystemCounterTrayIcon
from SslNetworkAccessManager import SslNetworkAccessManager
from PersistenceCookieJar import PersistenceCookieJar



class GmailWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.cookieJar = PersistenceCookieJar(QSettings("POWERUMC", "GmailTray"))
        
        self.onLoad();

    
    def onLoad(self):
        self.menuBar().hide()
        self.menuBar().close()
        self.resize(500, 600)
        
        
        # SSL 구
        sslcfg = QSslConfiguration.defaultConfiguration()
        ca_list = sslcfg.caCertificates()
        ca_new = QSslCertificate.fromData('CaCertificates')
        ca_list += ca_new
        
        sslcfg.setCaCertificates(ca_list)
        sslcfg.setProtocol(QSsl.AnyProtocol)
        QSslConfiguration.setDefaultConfiguration(sslcfg)
        

        # WebView 구성
        QNetworkProxyFactory.setUseSystemConfiguration(True)
        set = self.ui.webView.settings().globalSettings()
        set.setAttribute(QWebSettings.PluginsEnabled, True)
        set.setAttribute(QWebSettings.AutoLoadImages, True)
        set.setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        set.setAttribute(QWebSettings.JavascriptEnabled, True)
        set.setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
        set.setAttribute(QWebSettings.JavascriptCanOpenWindows, True)


        # 툴바 구성
        toolbar = QToolBar('Command Toolbar', self)
        toolbar.addActions(self.ui.menuCommand.actions())
        
        toolbar.addSeparator()
        toolbar.addActions(self.ui.menuCommand.actions())
        
        self.addToolBar(toolbar)

        self.ui.actionGo_Home.triggered.connect(lambda: ())
        self.ui.actionRefresh.triggered.connect(lambda: ())
        self.ui.actionNext.triggered.connect(lambda: ())
        self.ui.actionPrevious.triggered.connect(lambda: ())
        self.ui.actionHelp.triggered.connect(lambda: ())
        self.ui.actionPreferences.triggered.connect(lambda: ())

        self.ui.actionHelp.setEnabled(False)
        self.ui.actionPreferences.setEnabled(False)




        # 트레이 아이콘 설
        traymenu = QMenu('TRAY MENU', self)

        
        if sys.platform == 'darwin':
            action_open = QAction('O&pen', self)
            action_open.triggered.connect(lambda: ())
            traymenu.addAction(action_open)
            traymenu.addSeparator()

        action_quit = QAction('Q&uit', self)
        action_quit.triggered.connect(lambda : ())
        traymenu.addAction(action_quit)

        tray = HostSystemCounterTrayIcon(QImage('facebook.jpg'))
        tray.setContextMenu(traymenu)

        tray.setIcon(QIcon('facebook.jpg'))
        tray.show()

        tray.activated.connect(lambda reason:())
        tray.messageClicked.connect(lambda: ())
        
        
        
        # SSL 설정
        manager = SslNetworkAccessManager(self)
        manager.setCookieJar(self.cookieJar)
        
        
