#_*_ coding: utf-8 -*-

import gtk
import webkit

view = webkit.WebView()

sw = gtk.ScrolledWindow()
sw.add(view)

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
win.add(sw)
win.set_title(u"实验楼")
win.show_all()

view.open("http://www.shiyanlou.com")
gtk.main()