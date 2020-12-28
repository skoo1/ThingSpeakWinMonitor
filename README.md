# ThingSpeakWinMonitor"

### Reference code: https://gist.github.com/guillaumevincent/d8d94a0a44a7ec13def7f96bfb713d3f

### It can be registered as a Windows Service and send cpu and memory usage to a thingspeak channel regularlly. 

### Put ThingSpeak API KEY for your channel in the code then start a service as below.

### It needs pyinstaller to conver the python to a Windows executable.
#### >> pip install pyinstaller
#### >> pyinstaller -F --hidden-import=win32timezone ThingSpeakLogger.py

### Register it as a service. Start, stop and remove as you want. You should do it in a console with admin privilege.
#### >> dist\ThingSpeakLogger.exe install
#### >> dist\ThingSpeakLogger.exe start
#### >> dist\ThingSpeakLogger.exe stop
#### >> dist\ThingSpeakLogger.exe remove

### You can make it start automatically in the service manager by changing the start type to Auto.

### Then, you can monitor your computer usage in you cell phone app, ThingView.

<img src=./images/example_01.jpg width=200>