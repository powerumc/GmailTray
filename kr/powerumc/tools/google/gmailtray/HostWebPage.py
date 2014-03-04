from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *

class HostWebPage(QWebPage):
    
    def __init__(self, parent):
        QWebPage.__init__(parent)
        
        self.var = []
        self.var.baseurl = []
        
        self.linkHovered.connect(lambda:())
        self.linkClicked.connect(lambda:())
        self.loadFinished.connect(lambda:())
        
        self.__onTimer()
        
    def dispose(self):
        self.disconnect(self)
        
    
    def __onTimer(self):
        
        QTimer.singleShot(5000, self, SLOT(self.__onTimer()))

        count = 0
        frame = QWebView(self.view().page().mainFrame())
        if( frame != None): return
        
        notifyCount = frame.findAllElements("span[class='count mfss fcw']").toList()
        
        for i in notifyCount.count():
            n = notifyCount.at(i)
            if n.isNull(): continue
            
            count += n.toInnerXml().toInt()

        
    
    def userAgentForUrl(self, qurl):
        pass
    
    
    def onLinkHovered(self, link, title, textContext):
        pass
    
    
    def onLinkClicked(self, url):
        pass
    
    
    def onLoadFinished(self, ok):
        pass
    
    
    def acceptNavigationRequest(self, frame, request, type):
        pass
    
    
    def createWindow(self):
        pass
    
    
    