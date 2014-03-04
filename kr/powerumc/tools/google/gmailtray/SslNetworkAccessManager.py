# coding: utf-8

from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4.QtCore import *


class SslNetworkAccessManager(QNetworkAccessManager):
    
    def __init__(self, parent):
        QNetworkAccessManager.__init__(parent)
        
        self.cookieJar = None
        
        self.__onInit()
    
    def __onInit(self):
        #self.finished.connect(self.__onCookieReplyFinished)
        #self.sslErrors.connect(self.__onHandleSslErrors)
        pass
        
    def __onCookieReplyFinished(self, reply):
        if reply.isFinished():
            variantCookies = reply.header(QNetworkRequest.SetCookieHeader)
            cookies = [variantCookies]
            
        self.cookieJar.setCookiesFromUrl(cookies)
        
        
        
    def __onHandleSslErrors(self, reply, errors):
        for e in errors:
            pass
        
        reply.ignoreSslErrors()