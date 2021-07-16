import time
import socket
import win32serviceutil
import servicemanager
import win32event
import win32service
import smtplib, ssl
import requests
import logging.handlers
from configparser import ConfigParser

log_file_path = "C:\\Users\\(Tu usuario)\\Documents\\noip.log"  # mention full path here
mylogger = logging.getLogger("TestLogger")
mylogger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(log_file_path)
mylogger.addHandler(handler)

class Noip(win32serviceutil.ServiceFramework):
    _svc_name_ = "Noip cambio"
    _svc_display_name_ = "Cambio de ip (servicio)"
    _svc_description_ = "Avisa si hubo un cambio en la ip publica"

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,servicemanager.PYS_SERVICE_STARTED,(self._svc_name_, ''))
        self.main()

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def envia_correo(self,n,v,local,password,destino,config2):
        port = 465
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(local, password)
                server.sendmail(local, destino, "(Modem 2) La ip ha cambiado de " + str(n) + " a " + str(v))
                config2.set('ip','ip',v)
                with open('C:\\Users\\CCT-RENATO\\Documents\\ip.ini', 'w') as configfile:
                    config2.write(configfile)
                server.quit()
        except Exception as err:
             mylogger.info("Un error ha ocurrido al tratar de enviar el correo " + str(err))

    def main(self):
        config = ConfigParser()
        config.read('C:\\Users\\CCT-RENATO\\Documents\\config.ini')
        noreply = config.get('config', 'local')
        destino = config.get('config','destino')
        passw = config.get('config','password')
        tiempo = config.getint('config','frecuencia');

        while self.isrunning:
            resultado = ""
            #revisa la ip publica
            try :
                resultado = requests.get("http://ifconfig.me/ip").text
                mylogger.info(resultado)
            except Exception as err:
                resultado = "error"
                print("Un error ha ocurrido al tratar de obtener la ip publica" + str(err))
            config2 = ConfigParser()
            config2.read('C:\\Users\\(Tu usuario)\\Documents\\ip.ini')
            ip = config2.get('ip','ip')
            print(ip)
            # si cambia se envia correo para avisar que cambio
            if resultado == "error":
                mylogger.info("Un error ha ocurrido al tratar de obtener la ip publica")
            elif resultado != ip :
                self.envia_correo(ip,resultado,noreply,passw,destino,config2)
            time.sleep(tiempo)

if __name__ == '__main__':
   win32serviceutil.HandleCommandLine(Noip)
