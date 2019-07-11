from ctypes import windll
import glob
import time

img = ""

pics = glob.glob(img)

user32 = windll.user32

while True:
	for pic in pics:
		user32.SystemParametersInfoW(20, 0, pic, 0)
		time.sleep(0.5)
