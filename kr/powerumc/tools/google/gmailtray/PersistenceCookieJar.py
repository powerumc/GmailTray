# coding: utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *


class PersistenceCookieJar(QNetworkCookieJar):
    
    def __init(self, parent, settings):
        QNetworkCookieJar.__init__(parent)
        
        self.settings = settings
        
        self.__onLoad(settings)
        
        
    def dispose(self):
        self.__onSave(self.settings)
        
    
    def __load(self, settings):
        data = self.settings.value("Cookie").toByteArray()
        self.setAllCookies(self.parseCookies(data))
        
        
    def __save(self, settings):
        list = self.allCookies()
        data = []
        
        for cookie in list:
            if( cookie.isSessionCookie() == False):
                data.append(cookie.toRawForm())
                data.append("\n")
                
        settings.setValue("Cookie", data)
        
        
    def __onSave(self, settings):
        self.save(settings)
        
        
    def __onLoad(self, settings):
        self.load(settings)