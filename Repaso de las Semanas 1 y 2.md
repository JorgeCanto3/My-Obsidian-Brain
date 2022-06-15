<h2>Repaso de las Semanas 1 y 2

En este documento repasaremos las  semanas 1 y 2 del [[Ciclo Especializado]]

---
<h3> La Nube

- La nubes es la entrega de servicios de computo através de internet
	- Son los servidores que utilizamos para diversas cosas como ver peliculas, jugar algun videojuego, no se refiere al almacenamineto
	
	- Todo esto es mediante un enrutamineto, al interactuar nosotros nuestra accion es recibida por el Modem o Router y de ahi lo manda al [[ISP]]  para posteriormente mandarlo al [[IXP]] y mandarlo al servidor correspondiente, si es para los servidores de Facebook, Microsoft, etc. 
	-
---
<h3> Azure

- Azure es el servicio de la nube de Microsoft que entrega servicios informaticos a través de internet
	- Esto incluye casi todos los servicios de Microsoft, desde videojuegos hasta la programas como Word etc
---
<h3>Alta disponibilidad

**Caracteristica más importantes de la nube**

- La Alta disponibilidad es la capacidad de los servidores esten disponibles 24/7, aunque tenga caerse pueda recuperarse este servicio
	- Dependiendo del SLA, las aplicacion de la nube pueden proporcionar un servicio continuo sin inactividad aparente incluso cuando se presentan fallas.
	
---
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
---
<h3>Agilidad

- Es la implementacion y configuracion rapida de recursos de la nube a medida que los requerimientos cambian.
	- Hace referencia a que tambien podemos cambiar los recursos, más grandes o más chicos dependiendo de la demanda.
---
<h3> Elasticidad

- Los recursos se pueden autoescalar dependiendo de la necesida actual. Siempre teniendo los recursos que necesitas. 
	- Esta propiedad de Azure nos permite adapatar nuestro servidor se "estire"  o escaleun poco más el servidor de manera automatica

	- Este autoescaladao es minimo y no puede ser a gran escala de manera automatica
---
<h3> Escalado 

- El escalamiento es la adaptabilidad manual de nuestros servidores para adecuarlo a la necesidad que requerimos. Con un limite pero este limite es mucho mayor al de la Elasticidad 

	- Existen dos tipos de escalados:
	
		- Escalado Vertical:
		
			- Es el incremento de la capacidad de computo agregando RAM o CPU al recurso
			
		- Escalado Horizontal :
		
			- Incremetno de la capacidad de cómputo agregando mas instnacias del mismo recurso 
---
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

---
<h3> Niveles de Servicio de la Nube

- Iaas **Infraestructure as a Service**


	- El Iass es un modelo de servicios es muy cercano a tener los servidores fisicos. El proveedor solo se encargara el hardware, las demas responsabilidades recaen sobre el cliente

		- Suele ser usado cuando:
			- Se quiere control total
			- Requiere una configuracion especifica
			- Quieres instalar lo que sea

- Pass **Platform as a Service**

	- Modelo de servicio en un entorno de alojamineto gestionado. El proveedor se encarga de las MV's y los recursos de red y el inquilino de las aplicaciones.

- Saas **Software as a Service**
 
	-  El proveedor de la nube birndara las aplicaciones y se encarga de ellas y el usuario solo provee y administra los datos 


<h4> Economia de Escala

Las economias a escala mientras más usemos la nube más ahorramos en Azure. 

----
<h3> Recursos 

- Azure funciona a base de recursos y lo podemos administrar en Azure con [Azure Portal](https://portal.azure.com/)
	
	- <h4>Grupo de recursos </h4>

		Existen los grupos de recursos que son contenedores logicos con los recursos necesarios para nuestra solucion. Es decir que cuando necesitemo recursos requerimos de un grupo de recursos y ahi incluiremos todos los recursos necesarios para nuestra solucion.

---
<h3> Regiones

- Las regiones son zonas geograficas del planeta que tiene (minimo) un centro de datos de azure o más

	<h4> Zona de Diposnibilidad </h4>
	
	- Las zonas de disponibilidad estan dentro de las regiones,  en estas regiones se cuenta con 3 centros de datos de microsoft que permite tener mejor rendimiento, un mejor SLA y que funcione como un seguro en caso de que alguno de estos tres centros de datos llegue a fallar. 
	
		- Son zonas especifica y las mas importantes son en EU y China

----
<h3> Compute 

-  Proporciona los servicios de computo o procesamiento bajo demanda

	- <h4> Azure Virtual Machines <br>
	Modelo de servicio: Iaas</h4>
			 Este servcio es una computadora usada de manera remota en nuestra computadora o bien "Una computadora dentro de otra". Podemos usarla para lo que necesitemos y es recomendable para extender nuestro centro de datos o para pruebas y desarrollo

	- <h4> Azure Virtual Machines Scale Sets <br>
	Modelo de servicio: Iaas </h4>
	 
		Este servicio nos permite controlar varias maquinas virtuales de una manera sencilla. 
		Podemos aumentar o disminuir nuestras maquinas virtuales o replicarlas. Basicamente admnistramos todo en chinga

	-  <h4> Azure Batch <br>
	Modelo de servicio: Iaas </h4>
	Batch es un servicio nos permite procesar lotes de gran informacion, brindandonos una gran potencia. Este servicio es informatica de alto rendimiento

	- <h4> Azure App Services<br>
	Modelo de servicio: PaaS  </h4>
		
		Este servicio de azure nos permite hacer un desarrollo web como API's, FrontEnd y BackEnd
---

###  [[Contenedores]] - Docker

- Los contenedores funcionan para poder correr nuestro codigo desde cualquier lugar al igual que lo podemos escalar

	- <h4>Azure Conteiner Instances (A.C.I.)<br>
	Modelo de servicio: PaaS </h4>
		Ejecuta contenedores no requiere de nada extra y es util cuando se moveran ambientes de un lugar a otro al cual puede que accedan muchos usuarios

	- <h4>Azure Kubernetes Services (A.K.S.)<br>
	Modelo de servicio: PaaS </h4>
	Los kubernetes son orquestradores, ellos controlan los contenedores de ACI. Hace  sencilla la administracion, implementacion y operaciones. Puede autoescalarse, dirigir el trafico, etc.


	- #### [[Azure Functions]] <br>Modelo de servicio: PaaS - [[ServerLess]] 
	
		Este servicio es serverless por lo tanto no requiere como tal un servidor porque solo subimos lo que requerimos. Azure Functions es un servicio en el cual ejecutamos codigo y se cobra por el tamaño y las veces que usemos este codigo. Util para microservicios como las API o IoT


- #### [[Azure Logic Apps]] <br>Modelo de servicio: PaaS - [[ServerLess]] 
	
	- Es muy similar a functions pero es un entorno visual/grafico, no usamos codigo solo pedimos lo requerido ya que cuenta con conectores prestablecidos y personalizables. Es util para automatizar un proceso o negocio


- #### [[Azure Virtual Desktop]] (A.K.S.)<br>Modelo de servicio: PaaS 
	
	- Virtual Desktop nos virtualiza un area de trabajo o bien un escritorio o tambien una aplicacion, ya no virtualiza más. Es para el usuario final y en cambio las MV's es para crear soluciones

<h3> Redes

- Todo aquello que conecta a azure y al mundo. Las redes son cables que esta por todo el mundo, en su mayoria cables submarinos. Las redes permiten pasar los datos hacia otros recursos y al mundo exterior


- #### [[Azure Virtual Network]]<br>Modelo de servicio: IaaS 
	
	- Permite que las rede en azure se comuniquen entre si y permite el enrutamiento de red, ademas del filtrado de trafico de red. Conecta maquinas virtuales con mayor facilidad

- #### [[VPN]]<br>Modelo de servicio: IaaS 
	
	- Los VPN es un medio por el cual los datos se cifran y de esta manera es mas seguro conectarse a redes desconocidas. Usa el mismo camino como si te conectaras a internet y este camino que se cifra una parte solo para ti.

- #### [[Azure VPN Gateway]]<br>Modelo de servicio: IaaS 
	
	- Este servicio conecta tu centro de datos  a azure de una manera privada, que brinda mas seguridad y privacidad

- #### [[Azure ExpressRoute]]<br>Modelo de servicio: IaaS 
	
	- Este servicio conecta tus datos de punto a punto, es un servicio muy similar pero solo cuenta con esa "Pequeña " diferencia. Nos da un acceso más rapido y más privada

- #### [[Azure Application Gateway]]<br>Modelo de servicio: PaaS 
	
	- Dirige el trafico de la red, controla la entrega de aplicaciones, ejemplo: Si yo requiero de imagenes o de cierta informacion se me enviara a ese servicio
	![[SharedScreenshot.jpg]]


- #### [[Azure CDN (Content Delivery Network)]]<br>Modelo de servicio: PaaS 
	
	- Red de serviodores que entregan el contendio. <br>Este servicio nos permite crear un servidor intermedio para evitar saturaciones, asi acercamos nuestro servicio a los clientes reduciendo el tiempo de espera y mejoramos el redimineto de nuestros servicios
		
	![[Captura de pantalla 2022-06-13 224600.jpg]]





