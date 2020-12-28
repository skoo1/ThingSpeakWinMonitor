import servicemanager
import socket
import sys
import win32event
import win32service
import win32serviceutil
import requests
import psutil

class ThingSpeakLogService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ThingSpeakLogService"
    _svc_display_name_ = "ThingSpeakLog Service"
    _svc_description_ = "ThingSpeak Logger by skoo"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            # threading.Timer(10, thingspeak_post).start()
            val_cpu_usage = psutil.cpu_percent()
            val_mem_usage = psutil.virtual_memory().percent
            BASEURL = 'https://api.thingspeak.com/update?api_key='
            THINGSPEAK_APIKEY = 'XXXXXXXXXXXXXX'   # <--- Put your API Key
            VALUES = '&field1={}&field2={}'.format(val_cpu_usage, val_mem_usage)
            postURL = BASEURL + THINGSPEAK_APIKEY + VALUES
            data = requests.post(postURL)
            with open('C:\\Users\\XXXXX\Works\ThingSpeakLogService.log', 'a') as f:   # <--- Put log file path
                f.write(postURL)
                f.write('\n')
            rc = win32event.WaitForSingleObject(self.hWaitStop, 20000)   # <--- Logging interval


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(ThingSpeakLogService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(ThingSpeakLogService)