# Seguridad en la Red de Azure

### Defensa en profundidad

El objetivo de la defensa en profundida es proteger la información y evitar que las personas no autorizadas no accedan a la misma y a su vez no puedean sustraerla.

Una estrategia para una defensa en profundiad es usar un serie de mecanismo para ralentizar el avance de un ataque dirigido par poder conseguir un acceso no autorizado a los datos

Las capas de defensa en profundidad son Seguridad fisica, Identidad y acceso, Perímetro, Red, Procesos, Aplicacíon y Datos. _Ejemplo grafico_

![[Pasted image 20220616152027.png]]

Cada capa cuenta con un rol:

- Seguridad Física 
	- Es la primer defensa para poder proteger el hardware informatico del centro de datos
		- La intención es que no se puedan omitir otras caás de seguridad y se controle apropiedamente la perdida o robo  

![[Pasted image 20220616160739.png]]

- Identidad y acceso
	- Garantiza que las identidades esten protegidas, para que solo se otorgue el acceso necesario y que se registren los cambio y los eventos de inicio de sesión
		- Controla el acceso a la infraestructura y el control de cambios.
		- Podemos usar el inicio de sesión único y la autenticación multifactor

- Perímetro  
	- Es la Proteccion frente a ataques basadoes en rede contra los recursops, los identifica, elimina las repercursiones y recibimos alertas sobre ellos.
		- Proteccion ante ataques de denegación de servicio distribuido (DDos) para poder filtrar ataques a gran escala que puedan causar una denegacion de servicios a los usuarios.
		- Usa firewalls perimetrales para identificar los ataques malintencionados contra la red y alertar sobre ellos.

- Red
	- Esta enfoca en limitar la conectivdad entre recursos para permitir solo lo necesario, limitando reducimos el riesgo de que los ataques se propaguen a otro sistme de la red. Es importante que:
		- Se Limite la comunicación entre recursos con el control de acceso y segmentación
		-  Deniegue de forma predeterminada.
		-  Restrinja el acceso entrante de Internet y limite el saliente cuando sea apropiado.
		-  Implemente conectividad segura a las redes locales.

- Procesos
	- Aseguira que los recusos del proceso estén seguro y que cuenten con los controles adecuados para minimizar los problemas de seguridad
		- Protege el acceso a las máquinas virtuales
		-    Implemente la protección del punto de conexión de los dispositivos y mantenga los sistemas revisados y actualizados.

- Aplicación
	-  Todos los equipos de desarrollo deberían asegurarse de que sus aplicaciones son seguras de forma predeterminada. En desarrollo es importante la seguridad para evitar vulnerabilidades en el codigo. Tenemos que:
		-  Garantiza que las aplicacioones sean seguras y esten libres de vulnerabilidades de seguridad
		- Almacene los secretos de aplicación confidenciales en un lugar seguro
		- Convierta la seguridad en un requisito de diseño en todo el desarrollo de aplicaciones.

-  Datos
	- A menudo, los requisitos legales dictan los controles y procesos que deben cumplirse para garantizar la confidencialidad, la integridad y la disponibilidad de los datos.
		- Controla el acceso a los datos empresariales y clientes que es necesario proteger
		- A menudo se intenta coneguir los siguientes datos
			- Almacenados en una base de datos.
			-  Almacenados en discos en máquinas virtuales.
			-   Almacenados en aplicaciones de software como servicio (SaaS), como Office 365.
			-   Administrados mediante el almacenamiento en la nube.
	
 Las capas proporcionan una guia para poder configurar la seguridad de las aplicaciones

#### Posicion de seguridad 

El nivel de seguridad es la capacidad que tiene una organizacion poder protegerse frente a amanezas de segurirdad y tambien la capacidad de responder ante estas amenzas. Para poder definir un nivel de seguridad se utiliza la confidencialidad, integridad y la disponibilidad que en ingles se conoce como CIA.

- **Confidencialidad**
	- Son los principios de privilegios minimos que implica restringir el acceso a la información únicamente a los usuarios a las que se concede acceso de forma explícita, solo al nivel necesario para realizar su trabajo
	
	- Inclute proteccion de :
		- Constraseñas
		- Contenido de correo electronico
		- Niveles de acceso a las aplicaciones
		- La infraestructura subyacente.

- **Integridad**
	- Sirve para evitar los cambios no autorizados en la informacion
		- En Reposo: Cuando se almacena
		- En tránsito: Cuando se transfieren de un lugar a otro, incluido desde un equipo local desde la nube
	- Para la transimsion de datos es común utilizar la creacion de una huella digital unica de los datos por parte del remitene mediante un algoritmo hash unidireccional
		- El hash se envia junto con los datos
	- El receptor vuelve a calcular los datos y los compara con el original para asegurarse de que no hubiera cambios o perdidas en el transito

- **Disponibilidad**
	- En este apartado nos tenemos que asegurar que los servicios funcionen y que solo puedan acceder los usuarios autorizados. 
		- Los _ataques por denegación de servicio_(DDos) están diseñados para degradar la **disponibilidad** de un sistema, lo que afecta a sus usuarios.


<h2> Servicios par proteger la Red de Azure

- [[Azure Firewall]]

- [[Azure DDos Protection]] 

- [[Grupos de seguridad de red]]

<h2> Combinación de servicios de azure para una seguridad de red copleta

<h3> Protección de la capa perimetral</h3>

La capa perimetral trata sobre la protección de los recursos de su organización frente a ataques basados en red

Identificar estos ataques, alertar a los equipos de seguridad adecuados y eliminar su impacto es importante para proteger la red

Por ello:

-  Use **Azure DDoS** Protection para filtrar los ataques a gran escala antes de que puedan causar una denegación de servicio para los usuarios.

- **Azure Firewall** para identificar los ataques malintencionados contra la red y alertar sobre ellos.

<h3> ## Protección de la capa de red</h3>

El enfoque está en limitar la conectividad de la red en todos los recursos para permitir solo la necesaria. Cuando reducimos la conectividad reducimos el riesgo de que un ataque se desplace.

Con los **grupos de red** podemos crear reglas para definir la comunicacíon entrante y salientes que se limita en esta capa.

Procedimientos recomendados:

- Limite la comunicación entre los recursos mediante la segmentación de la red y la configuración de controles de acceso

-   Deniegue de forma predeterminada.

-   Restrinja el acceso entrante de Internet y limite el saliente cuando sea apropiado.

-   Implemente conectividad segura a las redes locales.

<h3> Combinacion de servicios </h3>

Con la combninacion podemos proporcionar mayor protección por capas.


- **Grupos de seguridad de red y Azure Firewall**

	- Azure Firewall complementa la funcionalidad de los grupos de seguridad de red. 
	
	- Los grupos de seguridad de red proporcionan filtrado de tráfico distribuido a nivel de red para limitar el tráfico a los recursos dentro de las redes virtuales de cada suscripción
	
	- FireWall proporciona protección de nivel de red y de aplicación en diferentes suscripciones y redes virtuales.


- **Firewall de aplicaciones web(WAF) de Azure Application Gateway y Azure Firewall**

	- WAF es una caracteristica de App  Gateway que protege a las apps webs centralizada en vulnerabilidades de seguridad comunes.

	- Azure Firewall proporciona lo siguiente:
		-  Protección entrante para protocolos que no son HTTP/S
		-  Protección de nivel de red de salida para todos los puertos y protocolos.
		-  Protección de nivel de aplicación para HTTP/S saliente.

 <h1> Resumen

-   Azure Firewall es un servicio de seguridad de red administrado y basado en la nube que ayuda a proteger los recursos en las redes virtuales de Azure.

-   Una red virtual de Azure es similar a una red tradicional con la que trabajaría en un centro de datos propio. Permite que las máquinas virtuales y otros recursos de proceso se comuniquen de forma segura entre ellos, con Internet y con las redes locales.

-   Un grupo de seguridad de red (NSG) le permite filtrar el tráfico de red desde y hacia los recursos de Azure dentro de una red virtual.

-   Azure DDoS Protection ayuda a proteger los recursos de Azure frente a ataques DDoS.
