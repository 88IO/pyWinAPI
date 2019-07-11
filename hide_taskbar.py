from ctypes import *

user32 = windll.user32

hWnd = user32.FindWindowW(u"Shell_traywnd", None)

user32.ShowWindow(hWnd, 0)
