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

...
