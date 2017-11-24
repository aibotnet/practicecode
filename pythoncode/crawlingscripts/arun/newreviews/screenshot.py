'''import gtk.gdk

w = gtk.gdk.get_default_root_window()
sz = w.get_size()
print "The size of the window is %d x %d" % sz
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
if (pb != None):
    pb.save("/home/aknauhwar/Desktop/screenshot.png","png")
    print "Screenshot saved to screenshot.png."
else:
    print "Unable to get the screenshot." '''

####this one is for selenium  fully working

from selenium import webdriver

#input = open('/home/aknauhwar/Desktop/URL_FILE.txt' , "r")
#urls = readlines(input)
urls=['https://stackoverflow.com/questions' , 'http://googleeee.com' ,'https://www.pricemachine.com/']
i=0 
for url in urls :
        browser = webdriver.Firefox()
        browser.get(url)
        browser.save_screenshot('/home/aknauhwar/Desktop/%d.png'%i)
        i=i+1
        browser.quit()
















'''from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://abshdjdkjdkdkdkdk.com/questions')
browser.save_screenshot('/home/aknauhwar/Desktop/screenie.png')
browser.quit()'''

























'''import webbrowser
import wx

wx.App()
link = "http://stackoverflow.com/questions"
webbrowser.get('firefox %s').open_new_tab(link)
screen = wx.ScreenDC()
size = screen.GetSize()
bmp = wx.EmptyBitmap(size[0], size[1])
mem = wx.MemoryDC(bmp)
mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
del mem
bmp.SaveFile('/home/aknauhwar/Desktop/screenshot.png', wx.BITMAP_TYPE_PNG)  '''