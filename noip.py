#!/usr/bin/python3

import time
import smtplib, ssl
import requests
from configparser import ConfigParser

  # For SSL
#password = input("Type your password and press enter: ")

# Lee la configuracion inicial
config = ConfigParser()
config.read('config.ini')
noreply = config.get('config', 'local')
destino = config.get('config','destino')
passw = config.get('config','password')
tiempo = config.getint('config','frecuencia');

#recibe la ip anterior, la nueva ip, el correo servidor y el correo de destino
def envia_correo(n,v,local,password,destino,config2):
	port = 465
	context = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
			server.login(local, password)
			server.sendmail(local, destino, "La ip ha cambiado de " + str(n) + " a " + str(v))
			config2.set('ip','ip',resultado)
			with open('ip.ini', 'w') as configfile:
				config2.write(configfile)
			server.quit()
	except Exception as err:
		print("Un error ha ocurrido al tratar de enviar el correo" + str(err))


while True:
	resultado = ""
	#revisa la ip publica
	try :
		resultado = requests.get("http://ifconfig.me/ip").text
		print(resultado)
	except Exception as err:
		resultado = "error"
		print("Un error ha ocurrido al tratar de obtener la ip publica" + str(err))

	config2 = ConfigParser()
	config2.read('ip.ini')
	ip = config2.get('ip','ip')
	print(ip)
	# si cambia se envia correo para avisar que cambio
	if resultado == "error":
		pass
	elif resultado != ip :
		envia_correo(ip,resultado,noreply,passw,destino,config2)
	time.sleep(tiempo)