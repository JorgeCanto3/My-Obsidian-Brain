<h1>Azure Virtual Network

----------
<h3> Caracteristicas

Modelo del servicio: IaaS

Algunas de las caracteristicas de las redes de azure las podemos encontrar [[Redes Virtuales de Azure]]. Aqui encontraremos caracteristicas como VPN, enrutaminetos, aisalmiento, ademas de conocer como funcionan las mismas  [[Redes Virtuales de Azure]].

Una red virual sirve para conectarse a una maquina virtual

Con este servicio podemos conectar dos redes virtuales

-------------

<h3> Creacion de una red virtual


Cuando se crea una red virtual de Azure, se configuran algunas opciones básicas. 

Tendrá la opción de configurar opciones avanzadas, como varias subredes, protección contra denegación de servicio distribuida (DDoS), host Bastion, firewall de Azure, puntos de conexión de servicio y uso de una puerta de enlace NAT.

<h6>Se configura lo siguiente al crear la red:

- Suscripción 

	- Esta opción solo se aplica si tiene varias suscripciones para elegir.

-  Grupo de recursos
	- Como cualquier otro recurso de Azure, una red virtual debe existir en un grupo de recursos. Puede seleccionar un grupo de recursos existente o crear uno.

-   Nombre de red
	-  El nombre de red debe ser único en la suscripción, pero no es necesario que lo sea globalmente. Elija un nombre descriptivo que sea fácil de recordar e identificar con respecto a otras redes virtuales.

-   Región
	-  Seleccione la región en la que quiere que exista la red virtual.
	
- Espacio de direcciones
	- Al crear la red se difine el espacio de direcciones internas con el formato de enrutamineto de interdominios sin clases (CIDR). Este espacio de direcciones debe ser único dentro de la suscripción y de cualquier otra red a la que se conecte.

- Subred
	- Entre los intervalos de direcciones de red virtual se pueden crear una o varias subrede que dividirán el espacio de direcciones de la red virtual. El enrutamineto dependerá de las rutas de trafico

- Puntos de conexion de servicio
	- Se habilitan los puntos en este apartado, se seleccionana en las lista los puntos de conexion de servicio de Azure que se quieren habilitar. 
	
	- Existen opciones como: Azure Cosmos DB, Azure Service Bus, Azure Key Vault, etc.

- Puerta de enlace NAT
	- Es un servicio de traduccion de direcciones de red (NAT) totalmente administrado y muy resistente 
	
	-  Virtual Network NAT simplifica la conectividad a Internet de salida para las redes virtuales. Cuando se configura en una subred, toda la conectividad saliente usa las direcciones IP públicas estáticas de Virtual Network NAT.

- BastionHost : Puede seleccionar habilitar o deshabilitar  en la red virtual.

	- BastionHost proporciona conectividad RDP y SSH segura e ininterrumpida a las máquinas virtuales directamente en Azure Portal a través de SSL.

- DDoS Protection estándar: Puede seleccionar habilitar o deshabilitar en la red virtual.
	
	- Aprotección contra DDoS estándar es un servicio prémium.

- Firewall :  Puede seleccionar habilitar o deshabilitar en la red virtual
	
	- Es un servicio de seguridad de red administrado y basado en la nube que protege los recursos de Azure Virtual Network. 

<h5> Configuraciones Adicionales

Mas opciones para confungurar la red local

- **Grupo de seguridad de red**:

	-  Los grupos de seguridad de red tienen reglas de seguridad que permiten filtrar el tipo de tráfico de red que puede entrar o salir de las interfaces de red y las subredes de red virtual.

- **Tabla de rutas**: 
	- Azure crea automáticamente una tabla de rutas para cada subred de una red virtual de Azure y agrega las rutas predeterminadas del sistema a la tabla.

-   **Delegación de subred**:
	-  Puede designar la subred que va a usar un servicio dedicado. 
