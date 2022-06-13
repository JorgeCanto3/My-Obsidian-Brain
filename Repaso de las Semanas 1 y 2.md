<h2>Repaso de las Semanas 1 y 2

En este documento repasaremos las  semanas 1 y 2 del [[Ciclo Especializado]]

<h3> La Nube

- La nubes es la entrega de servicios de computo através de internet
	- Son los servidores que utilizamos para diversas cosas como ver peliculas, jugar algun videojuego, no se refiere al almacenamineto
	
	- Todo esto es mediante un enrutamineto, al interactuar nosotros nuestra accion es recibida por el Modem o Router y de ahi lo manda al [[ISP]]  para posteriormente mandarlo al [[IXP]] y mandarlo al servidor correspondiente, si es para los servidores de Facebook, Microsoft, etc. 

<h3> Azure

- Azurees el servicio de la nube de Microsoft que entrega servicios informaticos a través de internet
	- Esto incluye casi todos los servicios de Microsoft, desde videojuegos hasta la programas como Word etc

<h3>Alta disponibilidad

**Caracteristica más importantes de la nube**

- La Alta disponibilidad es la capacidad de los servidores esten disponibles 24/7, aunque tenga caerse pueda recuperarse este servicio
	- Dependiendo del SLA, las aplicacion de la nube pueden proporcionar un servicio continuo sin inactividad aparente incluso cuando se presentan fallas.

<h3> Acuerdo de Nivel de servicio o
(SLA Server Level Agreement) 

- El SLA es el porcentanje de disponibilida y rendimiento de los recursos durante un tiempo determinado. 
	- Si el servicio llega a fallar mas de lo establecido se puede reducir costos de los servicios al reclamar al proveedor
	
	- Operacion para obtner el Tiempo de no disponibilidad
		- Tno = Tmax - (Tmax * SLA)
			- Ejemplo:
				- 99.9% de SLA garantizado en Bot Services por Mincrosoft
				- Contamos con 43,200 min al mes
				- La formula quedaria de la siguiente manera:
					- Tno =  43,200 - (43,200 * 0.999)
						- Queda .999 porque es un porcentaje
						
<h3>Tolerancia a Fallos

_Este servicio va enlazado a la Alta Dosponibilidad y al SLA_
	
- Tomar ventaja de los servicios de respaldo, replicación de datos y geodistrribucion de la nube. Tus datos estan seguros en caso de desastre
	- Cuando hay un error se recupera
	
	- Cuenta con replica de datos para no notar ese fallo
	
<h3>Agilidad

- Es la implementacion y configuracion rapida de recursos de la nube a medida que los requerimientos cambian.
	- Hace referencia a que tambien podemos cambiar los recursos, más grandes o más chicos dependiendo de la demanda.

<h3> Elasticidad

- Los recursos se pueden autoescalar dependiendo de la necesida actual. Siempre teniendo los recursos que necesitas. 
	- Esta propiedad de Azure nos permite adapatar nuestro servidor se "estire"  o escaleun poco más el servidor de manera automatica

	- Este autoescaladao es minimo y no puede ser a gran escala de manera automatica

<h3> Escalado 

- El escalamiento es la adaptabilidad manual de nuestros servidores para adecuarlo a la necesidad que requerimos. Con un limite pero este limite es mucho mayor al de la Elasticidad 

	- Existen dos tipos de escalados:
	
		- Escalado Vertical:
		
			- Es el incremento de la capacidad de computo agregando RAM o CPU al recurso
			
		- Escalado Horizontal :
		
			- Incremetno de la capacidad de cómputo agregando mas instnacias del mismo recurso 

<h3> Modelos de Ingreso

- La cantida de dinero con la que se cuenta para poder utilizar estos recuros.

- Existen dos tipos de modelo de ingreso:
	
	- CapEx (Capital Expenditure):
	
		-  Es el gasto inicial de dinero en infraestructura fisica que se deduce a lo largo del tiempo
		
			- Aqui la responsabilidad es total  sobre el dueño
				
				- Daños, robos, extensiones
				
		- Este tipo de nube se le conoce como **Nube Privada**
		
	-  **Nube Privada**
		- La nube privada es el recurso informatico excluisvo de los usuario de una empresa u organizacion la cual se encarga de el consumo de electricidad, seguridad y mantenimiento
		
		- Ademas de contar con el control total de los servicios
			
	- OpEx (Operational Expenditure)

		- Gasto de dinero en servicios o productos en el momento y se factura por ellos al momneto. NO hay inversion inicial
		
			- Gasto Opertaivo por el uso de un servicio

			- El tipo de nube OpEx siempre sera ** Nube Publica**
			
	- **Nube Publica**
	
		- La nube publica es aquel servicio que se ofrece a través de la red de internet pública y están disponibles para cualquira que quiera comprarlos, es decir, conseguir servicios de nube de terceros como Microsoft Azure  
				
	- **Nube Hibrida**
	
		- Entorno que comnina una nube publica con una nube privada, lo que permite compartir datos y aplicaciones entre ellas
			- Suele ser necesaria cuando por regulacion necesitas los datos dentro del país o extender la nube

<h3> Niveles de Servicio de la Nube

- Iaas **Infraestructure as a Service**


	- El Iass es un modelo de servicios es muy cercano a tener los servidores fisicos. El proveedor solo se encargara el hardware, las demas responsabilidades recaen sobre el cliente

		- Suele ser usado cuando:
			- Se quiere control total
			- Requiere una configuracion especifica
			- Quieres instalar lo que sea

- Pass **Platform as a Service**

	- Modelo de servicio en un entorno de alojamineto gestionado. El proveedor se encarga de las MV's y los recursos de red y el inquilino de las aplicaciones.
	