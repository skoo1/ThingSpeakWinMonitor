# ThingSpeakWinMonitor"

### Reference code: https://gist.github.com/guillaumevincent/d8d94a0a44a7ec13def7f96bfb713d3f

### It can be registered as a Windows Service and send cpu and memory usage to a thingspeak channel regularlly. 

### It needs pyinstaller to conver the python to a Windows executable.
#### >> pip install pyinstaller

### Register it as a service, start, stop and remove as you want.
#### >> dist\ThingSpeakLogger.exe install
#### >> dist\ThingSpeakLogger.exe start
#### >> dist\ThingSpeakLogger.exe stop
#### >> dist\ThingSpeakLogger.exe semove

### You can make it start automatically in the service manager by changing the start type to Auto.