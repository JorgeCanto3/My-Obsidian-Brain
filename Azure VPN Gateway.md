<h1> Azure VPN Gateway

<h2> Descripición

<h2> Caracteristicas

<h4>Puertas de enlace de VPN
-
- Una puerta de enlace de VPN es un tipo de enlace de red virtual. En Azure VPN Gateway se implementan en una subred dedicada de la red virtual y permiten la conectividad siguietnte:

	-   Conectar los centros de datos locales a redes virtuales a través de una conexión de _sitio a sitio_.
	
	-   Conectar los dispositivos individuales a redes virtuales a través de una conexión de _punto a sitio_.
	
	-   Conectar las redes virtuales a otras redes virtuales a través de una conexión _entre redes_.

	![[Pasted image 20220606193026.png]] 
	_Aqui podemos ver como la informacion es mandada a través de un tunel privado mientras cruza el internet_

- Todas las transferencias de datos se cifran en un túnel (**como podemos ver en la imagen de ariba**). Sin embargo solo se puede implementar una instancia de VPN en cada red virtual, pero podemos usar una puerta de enlace par conectarse a varias ubicaciones.

- La implementacion de una instancia de VPN Gateway tenemos que especificar le tipo de red privada virtual, basa den directivas o en rutas (La diferencia radica en como se especifica el tráfico que se va a cifrar.), ambos tipos de VPN en Azure usan una clave previamente compartida para autentificar, tambien se basan en el intercambio de claves por red (IKE)(_El IKE se usa para establecer una asociación de seguridad (un contrato del cifrado) entre dos puntos de conexión_ ),en las versiones 1 o 2 y en el protocolode seguridad de Internet (IPsec). Despues la asociación se passa al conjunto de IPsec, que cifra y decrifra, para desencapsular los datos

<h4> Redes privada virtuales basadas en directivas

- Las instancias de VPN gateway basadas en directivas, especifican de forma estática la dirección IP de los paquetes que se deben cifrar a través de cada túnel. Este tipo de dispositivo evalúa cada paquete de datos en función de los conjuntos de direcciones IP para elegir el túnel a través del cual se va a enviar el paquete.

	-   Uso del _enrutamiento estático_, en el que las combinaciones de prefijos de dirección de ambas redes controlan cómo se cifra y descifra el tráfico a través del túnel VPN. El origen y destino de las redes de túnel se declaran en la directiva y no necesitan declararse en las tablas de enrutamiento.

<h4> Redes privada virtuales basadas en rutas

- Con las puertas de enlace basadas en rutas, los túneles IPSec se modelan como una interfaz de red o una interfaz de túnel virtual. El enrutamiento IP decide cuál de estas interfaces de túnel se va a usar al enviar cada paquete. Las redes privadas virtuales basadas en rutas son el método preferido para conectar dispositivos locales. Son más resistentes a los cambios de la topología, como la creación de subredes.

	- Uso de VPN gateway basada en rutas
	
		-   Conexiones entre redes virtuales
		-   Conexiones de punto a sitio
		-   Conexiones de varios sitios
		-   Coexistencia con una puerta de enlace de Azure ExpressRoute
	
	- Puede usar _protocolos de enrutamiento dinámico_, donde las tablas de enrutamiento y reenvío dirigen el tráfico a diferentes túneles IPSec. Los paquetes de datos se cifran en función de las tablas de enrutamiento de red que se crean de forma dinámica mediante protocolos de enrutamiento, como el Protocolo de puerta de enlace de borde (BGP)

<h4> Recursos necearios para implementar VPN Gateway

-   **Red virtual**. Implemente una red virtual que tenga suficiente espacio de direcciones para la subred adicional que necesitará para la instancia de VPN Gateway. 
    
-   **GatewaySubnet**. Implemente una subred llamada `GatewaySubnet` para la instancia de VPN Gateway. 

-   **Dirección IP pública**. Cree una dirección IP pública dinámica de SKU básico si usa una puerta de enlace que no tenga en cuenta la zona. Esta dirección proporciona una dirección IP pública enrutable como destino para el dispositivo VPN local.
    
-   **Puerta de enlace de red local**. Cree una puerta de enlace de red local para definir la configuración de la red local; Esta información la usa la instancia de VPN Gateway con el fin de enrutar paquetes destinados para las redes locales a través del túnel IPSec.
    
-   **Puerta de enlace de red virtual**. Cree la puerta de enlace de red virtual para enrutar el tráfico entre la red virtual y el centro de datos local u otras redes virtuales.
    
-   **Conexión**. Cree un recurso de conexión para crear una conexión lógica entre la instancia de VPN Gateway y la puerta de enlace de red local.

 
    ![[Pasted image 20220607180527.png]]


<h3> Recursos locales necesarios


-   Un dispositivo VPN que admita instancias de VPN Gateway basadas en directivas o en rutas.
-   Una dirección IPv4 de acceso público (enrutable por Internet).