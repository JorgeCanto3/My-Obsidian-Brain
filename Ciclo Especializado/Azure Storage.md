# Azure Storage
	Azure Storage no es lo mismo que los 
	servicios de base de datos de Azure.
	
Azure Storage es un servicio que puede se usado para alamacenar archivos, mensajes , tablas y otros tipos de infromación . Este puede ser usado en sitios wbe, apps moviles, apps de escritorio. 

Ademas Azure Storage es usado en maquinas virtuales para infraestructura como servicio (SaaS) y en servicios de la nube de plataforma como servcio (PaaS)

Azure Storage cuenta con distintos servicios como:

-  [[Azure Blob Storage]]
	- Es un servicio que sirve para almacenar una  cantidad masivade datos no estructurados como texto o binario
	
- [[Azure FIle Storage]]
	-  Servicio que ofrece manejo total de archivos compartidos en la nube.

- [[Azure Disk Storage]] 
	-  Servicio que provee discos para las maquinas virtuales y aplicaciones para accesar y usarlo como se necesite. Ofrece HDD y SDD

- Azure Table Storage
	-  Ofrece un base de datos NoSQL ( Base de datos no relacional)
	
-[[ Azure Queue Storage ]]
	- Ofrece mesanjes asincrónicos para la comunicacion entre aplicaciones y recursos

Existen tres metodos para mejorar el manejo de la informacion de nuestro sitio web:

- Cold
	-  Con este metodo guardaremos la informacion que es poco frecuentada como datos de los usuarios o informacion que lleva almacenada al menos 30 dias

- Hot:
	- Con este metodo guardaremos la informacion que es muy frecuentada como imagenes para nuestra pagina

- Archive:
	-  Con este metodo guardaremos la informacion que es muy poco frecuentada como datos o informacion que lleva almacenada al menos 180 dias