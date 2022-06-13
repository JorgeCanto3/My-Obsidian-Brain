# Azure File Storage
## _Aspectos Basicos_

Azure Files ofrece recursos compartidos de archivos totalmente administrados en la nube a los que se puede acceder mediante los protocolos del Bloque de mensajes del servidor y Network File System.

Estos recursos compartidos se pueden montar en Windows, Linux y MacOS en la nube o de manera local. Cualquier número de roles o máquinas virtuales de Azure puede montar y acceder simultáneamente al recurso compartido de almacenamiento de archivos. 

![[Pasted image 20220608184249.png]]

_Azure Files garantiza que los datos se cifren en reposo, y el protocolo SMB garantiza que los datos se cifren en tránsito. Ademas una cossa que diferencia a Azure de otros archivos compartidos es que puedes tener acceso en cualquier lugar del mundo mediante una direccion URL o token de SAS para permitir acceso a un recurso privado por cierto tiempo _