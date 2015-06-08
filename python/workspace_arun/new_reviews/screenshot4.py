#  this one is final one we are using
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file):
        
                self.load(QUrl(url))
                self.wait_load()
                # set to webpage size
                frame = self.page().mainFrame()
                self.page().setViewportSize(frame.contentsSize())
                # render image
                image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
                painter = QPainter(image)
                frame.render(painter)
                painter.end()
                print 'saving', output_file
                image.save(output_file)
                
        

    def wait_load(self, delay=3):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True



s = Screenshot()
        
url=sys.argv[1]
count=sys.argv[2]
print url
s.capture(  url,'/home/aknauhwar/Desktop/testing/%s.png'%count ) # location where to store the png files
    


