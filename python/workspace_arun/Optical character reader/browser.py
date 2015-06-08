'''import sys
import wx
import wx.webkit       

theApp = wx.PySimpleApp(0)
theFrame = wx.Frame(None, -1, "", size=(640,480))
w = wx.webkit.WebKitCtrl(theFrame, -1)
w.LoadURL(sys.argv[1])
theFrame.Show()
theApp.MainLoop()'''

# it is standalone browser created in python using webkit , see its magixc , but doent have any functionality like history , go back etc becoz it has just began

#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://stackoverflow.com/questions"))
web.show()

sys.exit(app.exec_())