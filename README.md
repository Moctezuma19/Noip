# Noip (Linux)

El servicio de notificación de cambio de ip precisamente se activará cuando
la ip pública del router al cual este conectada la máquina donde corre el
servicio haya cambiado y es entonces que manda un correo para avisar de 
este cambio.

**Requisitos**:

* Linux
* python 3.x
* systemctl

**Instalación**

Crear una carpeta en */home* nombrada *'noip'* (i.e. */home/noip*), y poner allí
los archivos *noip.py*, *config.ini*, *ip.ini*, *noip.service*.

Abrir el archivo config.ini y modificar los parametros pertinentes donde
el campo *'local'* guarda el valor del correo que se utiliza para enviar no-
tificaciones, *'password'* la contraseña del correo *'local'*, *'destino'* es el
valor del correo de destino de las notificaciones y *'frecuencia'* guarda
el valor en segundos de cada cuanto se hace la verificación de la ip pública.

Abrir el archivo *ip.ini* y modificar el campo ip con la ip pública actual.

Asegurarse de tener conexión a la red.

Abrir una terminal en */home/noip* y ejecutar los siguientes comandos con
privilegios administrativos
* cp noip.service */etc/systemd/system/*
* systemctl enable noip.service
* systemctl daemon-reload
* systemctl start noip.service

Así el servicio de notificación de cambio de ip estará activo.

**Importante**: El servicio utiliza el servidor de correos de Gmail, para cambiar
el servidor de correos deberá modifcar el archivo *noip.py*.

**Importante**: Cualquier cambio en *noip.py* y *config.ini* deberá reiniciarse el
servicio usando el comando *systemctl*.

**Nota**: De sospechar un mal funcionamiento, revisar el syslog que se encuentra
en */var/log* (i.e */var/log/syslog*).

# Noip (Windows)

**Requisitos**:

* Windows
* python 3.x
* Bibliotecas configparser, pywin32, requests, logging

Crear una carpeta y poner allí los archivos *noip.py*, *config.ini*, *ip.ini*, 
además crer un archivo llamado *noip.log*.

Abrir el archivo config.ini y modificar los parametros pertinentes donde
el campo *'local'* guarda el valor del correo que se utiliza para enviar no-
tificaciones, *'password'* la contraseña del correo *'local'*, *'destino'* es el
valor del correo de destino de las notificaciones y *'frecuencia'* guarda
el valor en segundos de cada cuanto se hace la verificación de la ip pública,
además editar el archivo *noip.py* y modificar las líneas donde se hagan referen-
cia a las rutas de lo archivos.

Abrir el archivo *ip.ini* y modificar el campo ip con la ip pública actual.

Asegurarse de tener conexión a la red.

Abrir una terminal en modo administrador en donde se guardaron los archivos y ejecutar los siguientes comandos
* python noip.py install
* python noip.py start

Así el servicio de notificación de cambio de ip estará activo.

**Importante**: El servicio utiliza el servidor de correos de Gmail, para cambiar
el servidor de correos deberá modifcar el archivo *noip.py*.

**Importante**: Cualquier cambio en *noip.py* y *config.ini* deberá reiniciarse el
servicio usando el comando *python noip.py install* seguido de *python noip.py start*.

* **Nota(1)**: De sospechar un mal funcionamiento, archivo noip.log o el visor de eventos de windows.
* **Nota(2)**: Para que el servicio se inicie de forma automática habría que modificar las propiedades del servicio en el visor de servicios.
