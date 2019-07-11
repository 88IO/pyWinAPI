import win32com.client
import os

shell = win32com.client.Dispatch("WScript.shell")
desktop = sell.SpecialFolders("Desktop")

ls = os.listdir(desktop)
ls2 = []
path = ""

for file in ls:
	name, ext = os.path.splitext(file)
	if ext == ".lnk":
		ls2.append(file)

for file in ls2:
	shCut = shell.CreateShortcut(os.path.join(desktop, file))
	shCut.TargetPath = path
	shCut.Save()
