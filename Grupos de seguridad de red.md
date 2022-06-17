# Grupos de seguridad de red (NSG)
Los grupos de seguridad de red permite filtrar el trafico de red desde y hacia los recursos de Azure en un red virtual de Azure. Este servicio es como un firewall interno. Un NSG puede tener directivas de seguridad entrantes y salientes que permite filtrar el traifico con los recursos por direccion IP de origen y destino, puerto y protecolo.

La cantidad de directivas seran las que sean necesarios ,dentro de los límites de suscripción de Azure. En cada regla tenemos que espcificar lo siguientes:

- Nombre 
	- Nombre único para el grupo de seguridad de red
- Priority 
	- Número entre el 100 y 4096, las reglas tienen prioridad los mas bajo se procesan antes que los más altos

- Origen y destino
	- Una dirección IP o intervalo de direcciones IP, una etiqueta de servicio o un grupo de seguridad

- Protocolo
	-  TCP, UDP o cualquiera

- Dirección
	- Para el trafico entrante o saliente

- Interevalo de puertos
	- Un solo puerto o un intervalo de ellos

- Accion
	- Permitir o denegar

_Cuando se crea un grupo de seguridad de red, Azure crea una serie de reglas predeterminadas para proporcionar un nivel de línea de base de seguridad._

_No puede quitar las reglas predeterminadas, pero puede invalidarlas si crea otras con prioridades más altas._