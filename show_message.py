from ctypes import *

user32 = windll.user32

user32.MessageBoxW(0, "さああああ", "message", 0x00000000)
