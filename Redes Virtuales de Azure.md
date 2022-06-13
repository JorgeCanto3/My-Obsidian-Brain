<h1>Redes Virtuales de Azure
----------------
Las redes virtuales permiten la comunicacion con los servicios entre si y con los usuarios de internet y con los equipos cliente en el entorno local.
Una red de Azure se puede considerar una extension de la red local con recursos que vincula otros recursos de Azure

La comunicacion entre servicios es segura, como la comunicacion entre MV's (Maquinas Virtuales). Para mayor seguirdad podemos poner nuestros endpoints (Puntos de Conexion) para proteger el trafico de los recursos mas importantes

Los Endpoints pueden ser creadors con: Azure Storage, Azure SQL Database, Azure Cosmos DB, Azure Database for PostgreSQL, Azure for MySQL. Ademas de proporcionar protección de las aplicaciones y las maquinas virtualers que hosperda frente a ataques y vulnerabilidades de seguridad 

<h3>Las redes de azure proporciona las siguintes funcionalidades:
-
- Aislamineto y segmentación 

	- La red virtual de Azure permite la creacion de varias redes virtuales aisladas.Cuando se configura uan red virtual se define un espaacio de direcciones IP privadas y publicas.
		- El  IP publico solo existe dentro de la red virtual y no se puede enrutar. Despues este mismo se puede dividir ese espacio de direcciones IP en Subredes y asignar parte del espacio de direcciones definido a cada subred con nombre 

- Comunicación con Internet
	-  Puede habilitar las conexiones entrantes desde Internet mediante la asignación de una dirección IP pública a la máquina virtual o colocando la máquina virtual detrás de un equilibrador de carga público.
	
- Comunicación entre recursos de Azure
	
	- Para hacer que los servicios se comuniquen los servicios de forma segura Azure nos proporciona dos formas:
	
		- Redes Virtuales:
			-  Con este servicio no solo podemos conectar maquinas virtuales, si no tambien otros recursos como apps servces, kubernets, escalados de maquinas, etc.
		
		- Puntos de conexion de servicio: 
			- Con esto podemos conectar otros tipos de recursos de Azure, como almacenamineto y bases de datos. Asi se permite vincular varios recursos de azur ocn las redes virtuales para poder proporcionar una mejor seguridad y enrutamiento optimo. 
	
- Comunicación con los recursos locales
	- Con Azure podemos vincular los recursos del entorno local y dentro de la suscripcion de azure. Podemos lograr la conectividad con tres mecanismos 
		- Redes privadas virtuales de punto a sitio
		
			- La conexion de una [[VPN]] consiste en establecer la conexion con la red corporativa desde un equipo ajeno a la organización.
			
			-  El equipo cliente inicia una conexión VPN cifrada para conectar ese equipo a la red virtual de Azure.
			
		- Redes privadas virtuales de sitio a sitio
			- Una VPN de sitio a sitio vincula un dispositivo  o puerta de enlace de VPN local con la puerta de enlacede VPN Azure en unra red virtual. La conexion se cifra y funciona a través de internet
			
		-	Azure ExpressRoute
			
			- ExpressRoute proporciona una conectividad privada dedicada a Azure que no viaja por internet

- Enrutamineto del trafico de red
	- Azure enruta el trafico en subredes de las redes virtuales conectadas, redes locales e internet. Se puede controlar el enrutamineto e invalidar del siguiente modo:
		
		- [[Tabla de rutas ]] 

			- Podemos crear tablas con rutas personalizada que controlen cómo se enrutan los paquetes entre las subredes
			
		- Protocolo de puerta de enlace de borde(BGP):
			
			- Funciona con puertas de enlace de VPN, Azure route Server o ExpressRoute para propagar las rutas BGP locales a las redes virtuales de Azure.

- Filtrado del tráfico de red

	- Se puede filtar el trafico por medio de subredes con los siguientes métodos:
		
		- Grupos de seguirdad de red
		
			-  Es un recurso de Azure que puede contener varias reglas de seguridad de entrada y salida, con las reglas podemos  permitir o bloquear el tráfico em función de factores. 
		
		- Aplicaciones virtuales de red: 

			- Es una maquina virtual (MV) especializada que se puede compara con un dispositivo de red protegido. Se ejerce una funcion de red determinada, como ejecutar un firewall. 
			
- Conexión de redes virtuales
	
	- El emparejamineto virtual nos ayuda a vincular redes virtuales entre si, este servicio  permite que los recursos de cada red virutal (RV) se comuniquen entre si. Las RV pueden ser de regiones distintas de manra que podemos crear una red global interconectada con Azure. 

	- Las rutas definidas por el usuario (UDR) son una actualización significativa de las redes virtuales de Azure que permiten un mayor control sobre el flujo de tráfico de red
	
		-  Este método permite a los administradores de red controlar las tablas de enrutamiento entre subredes dentro de una red virtual, así como entre redes virtuales.

	

