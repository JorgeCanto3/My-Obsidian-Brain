# Track 2
#### Modulo 2 

- Servicio de Redes, Computo y Bases de daros

## Servicios de computo

- Proporcionan servicios de computo o procesamiento bajo demanda

---------

### Maquinas Virtuales

- Que es una **MV** o **Maquina Virtual**

	- Es una computadora que esta dentro de otra, es una emulacion del hardware dentro de una computadora.

	- Estas Maquina Virtuales son un servicio IaaS, contamos con el control total del sistema operativo, es util para cuando necesitamos tener control de todo el software y es util para extender el centro de datos

	- El servicio de Azure se le conoce como Azure Virtual Machines  
	
	- Sirve par economisar o evitar más gasto CapEx

#### Instancias Reservadas

Se ofrecen Reservas de Azure en muchos servicios como una forma de reducir el costo. Se reserva una capacidad de prepago para un período, generalmente de uno o tres años.

--------

 - **Azure Virtual Machines Scales Sets**
	 - Controlamos varias maquinas virtuales facilmente, podemos aumentarla y disminuirlas. Es util para administrarlas todas y replicarlas con facilidad.
	 - Nos ahorramos trabajo



- **Azure Batch 

	- Es un IaaS y es un servico de Informatica de alto rendimiento, donde procesamos una gran cantidad de datos en lotes en paralelo
	- Procesamos grandes cantidades de informacion como videos, un ejemplo seria mandar video para hacer una revision de contedio pero este video se divide en lotes para poder procesarlo en paralelo



**Azure App service**

- **Funcion**
	- Es un servicio de Tipo PaaS donde se habilitan sitios web, Paginas o habliaciones web

- Una pagina tiene:
	- **FrontEnd**

		- El FrontEnd se puede definir como todo aquello visual que podemos ver e incluso interactuar

	- **API**
		- Un API conecta las partes de FrontEnd y BackEnd para hacer peticiones de Front a Back. 


	- **BackEnd**

		- El BackEnd es todo el proceso que se lleva acabo para que el FrontEnd pueda funcionar.

-----------

## **Contenedores**

Los contendores virtualizan la pagina

**Azure Container Instance**

- Es un servicio de tipo PaaS, este servicio ejecuta contendeores, no requiere de una MV y nada adicional.

- Los contendores sirven para cuando moveremos nuestros  de un lugar a otro

**Azure Kubernetes Services:**

- Es un servicio de tipo Paas, que controla los contenedores de **Azure Container Instance**, es util para cuando las aplicaciones son altamente escalables

- Se pueden Auto escalar los contenedores o reducir la app para evitar costos y puede implementar los nodos

----
## **Informatica sin Informacion (Severless)**

La informatica sin servidor abstrae toda la infraestructura para ejecutar un servicio

**Azure Functions**

- Paas Serverless

- Sirve para ejecutar codigo y cobra por ejecutar y por el tamaño de la ejecucion

- Util para mensajeria, Iot o un microservicio 

**Azure Logic Apps**

- Paas Serverless

- Enfoque para automatizar procesos, cobra por evento y por el tamaño del evento. Responden ante Triggers que cuando se cumplan se ejecuta una acción

- Cuenta con conectores prestablecidos y personlizado


#### Azure Virtual Desktop
Es un servicio Paas, que virtualiza escritorios en la nube.

Es ideal para cargar aplicaciones y no hay nada que configurar y entregarla a un usuario

Es similar a Virtual Machines pero en VM virtualiza computadoras en la nube

----

## Redes en Azure

El internet en su mayoria es por medio de redes Submarinas, la red es lo que permite sacar nuestras maquinas virtuales hacia el mundo y conectarlas entre si. Tambien los servicios de red nos permite no pasar o no dejar que se comuniquen maquinas virtuales

**Azure Virtual Network**

- Servicio IaaS

- Nos permite conectar maquinas virtuales entre si. Permitiendo el enruitamiendo de trafico ded red, tambien permite el filtrado de red

- SubNet par conectar las maquinas virtuales dentro de las redes virtuales

**[[Azure VPN Gateway]]**

- Canal cifrado y seguro para que pasen nuestros datos, es una red privada Virtual

**[[Azure ExpressRoute]]**

Es un servicio IaaS, similar a VPN gateway pero es un servicio de punto a púnto 

**[[Azure CDN (Content Delivery Network)]]**

- Servicio PaaS
- Red de servidores que entregan el contenido, sirve para mejorar el rendimiento, escala y mejora las apps web
- Envia o distribuye a los usuario para que el servidor de origen tenga menos trafico

---------

## Datos y Almacenamiento
**Un requisito para usar los servicios de almacenamiento es crear**


Azure Blob Storage

Almacena Datos 

Sirve para compartir y controlar la informacion entre maquina virtuales, y sirve para faciilitar la migracion


Azure Disk Storage

Discos para maquinas virtuales pueden ser SDD o HDD 

Azure SQL DataBase

Servicio de tipo Paas

Azure Cosmos DB

Servicio de Tipo PaaS

Azure SQL Mange Instances

**Azure DataBase for MySQL**

Azure Database for PostagreSQL

-----

## Big Data
4TB Pa arriba

**Azure Synapse Analytics**

Azure Bricks

**Azure DataFactory**

----

Requisitos Minimos para crear un recursos de Azure:

- Suscripcion
- Nombre
- Grupo de recursos
- Region