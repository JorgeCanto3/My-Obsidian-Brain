# Sesion 6 del [[Ciclo Especializado]]
## Datos y Almacenamiento
Existe un diferencia entre los datos y el almacenamiento, ya que los datos son toda aquella informacion de los usurarios, mientras que en el alacenamiento de guardaran los programas, archivos, etc.

### Storage 
El storage proporciona servicios de almacenamiento de archivos y objetos

Es complicado accder al almacenamiento a menos  que tengamos permisos o una clave para poder a acceder a esa informacion 

### Servicios de Almacenaminetno
#### Cuenta de Almacenamiento

Para poder usar los servicios de Azure de Almacenamiento requerimos una cuenta de Almacenamiento. La cuenta de almacenamineto es la que contiene todos los servicios de Storage

**Todos los servicios de  Almacenamiento (Storage) de Azure SON IaaS** 

**_Bases de Datos NO_**

Este servicio tiene Alta disponibilidad, Durabilidad, Seguridad y Escalabilidad

##### [[Azure Blob Storage]]

**IaaS**

Un blob son archivos, cualquier tipo de archivos y no se limita a ningun formato.

Es un servicios donde se pueden almacenar archivos de gran tamaño, controlando el acceso al mismo.

Puede almacenar hasta archivos de 8 TB y sirve como respaldo de las maquinas virtuales de hasta 8 TB. 

Además esta optimizado para hacer streaming de video o audio.

Sirve más como un respaldo ante los servicios. 

##### [[Azure File Storage]]
**Iaas**
 
 File Storage sirve para almacenar archivos más pequeños, más privados y poder controlar más el acceso a la información. Puede funcionar como disco duro compartido para todas las maquinas virtuales

Tambien sirve para migrar de local a la nube

Sirve para crear paginas Web 

Util para compartir archivos a  muchos usuarios

Su alamcenamineto es grande pero no tanto como [[Azure Blob Storage]]

Controlamos mejor los archivos


##### [[Azure Disk Storage]]
**IaaS**

Discos para maquinas virtuales para almacenamiento.

Disk Storage es el servicio donde se almacena nuestra informacion de la maquina virutal. Una maquina virtual cuenta con Dos discos, uno dentro del S.O y otro fuera que es el disco de Datos.

Puede ser un HDD, SSD, SSD Premium y Ultra Disks.

##### [[Azure Queue Storage]]
**IaaS**

Ordena los mensajes en cola, es una fila virtual que va mandando los mensajes que van entrando por orden, en primero que entra es el primero que sale 

Puede almacenar gran cantidad de mensajes pero solo de 64 KB, Muchos mensajes pero de poco almacenamiento por mensaje

**Practica Min 36**



-------------
#### Bases de Datos

Lugar donde podemos almacenar datos de los usuarios como correo, nombre dee usuario, las bases de datos nos dan una amplia variedad de tipos y volumnes de datos

SQL (Structured Query Languange)

Una Base de Datos estructura y relacional requiere una estructurada, un orden de la informacion donde se ordena la informacion por columnas y las columnas se relacionan entre si

**Todas las bases de datos SON PaaS, Porque ya esta instalada en Azure**

##### [[Azure SQL Database]]
**PaaS**

Es una base de datos estructurada y relacional, Ejecuta la ultima version Microsoft SQL Server.

Se usa para saber que vamos a guardar Exactamente, los datos que registraremos.

##### [[Azure Cosmos DB]]
**PaaS**

No estructurada, no relaciona

Sirve para realizar guardado de datos rapidos a la vez que consultas de datos rapidas

Soporta  MongoDB, Cassandra, Gemlin

##### [[Azure SQL Manage Instances]]
**PaaS**


Es una base de datos administrada por microsoft. Las copias de seguridad, configuracion lo hace microsoft

Es más caro pero es menos trabajo

Gracias a que es administrado por Microsoft se ofrece Mayor disponibilidad y SLA, ademas de contar con copias automáticas en Blob Storage 

##### [[Azure SQL  Virtual Machines]]
**Iaas y PaaS al mismo tiempo**

SQL dentro de una maquina virtual, podemos usar las versionaes completas de SQL server

Es lo mismo que [[Azure SQL Database]] pero nos encargamos de todo menos el hardware y es util para migrar desde On-Premises y cuando requerimos una configuracion especifica


##### [[Azure Database for MySQL]]
**PaaS**

Base de datos igual a [[Azure SQL Database]] pero con MySQL es diferente motor pero es la misma funcion, se cobra por la infraestructura de Azure como la Alta disponibilidad, las copias de seguridad automaticas, etc


##### [[Azure Database for PostgreSQL]]

**PaaS**

Base de datos igual a [[Azure SQL Database]] pero con PostgreSQL, OpenSource pero puede venir con un Servidor Único basico de uso general u optimizado para la memoria o con HyperScale citus para admitir una gran cantidad de datos

Tiers de PostgreSQL

- Basic
	- Uso
		- Cargas de trabajo ligeras en la computadora y en el rendimiento
	- Carcateristicas
		- GEN4,5
		- Cores 1,2
		- Memory per core 2gb
		- Storage Size 5gb to 1tb
		- DataBase backup 7 a 35 dias
- General purpose
	- Uso
		- Utilizado para cargas empresariales que requieren balanceo entre computadora y memoria con escalabilidad
	- Caracteristicas
		- GEN4,5
		- Cores 2, 4, 8, 16, 32, 64
		- Memory per core 5gb
		- Storage Size 5gb to 1tb
		- DataBase backup 7 a 35 dias
- Memory Optimized
	-Uso
		- Bases de datos con alto rendimiento para cargas de memoria que requieren un rendimineto rapido apra la transaccion y precesamiento 
	- Caracteristicas
		- GEN 5
		- Cores 2, 4, 8, 16, 32
		- Memory per core 10gb
		- Storage Size 5gb to 1tb
		- DataBase backup 7 a 35 dias

**Practica**

-------------
#### Big Data

La big data es cuando requerimos hacer un procesamineto y analisis de grandes cantidades de registros. Para 4tb o más

##### [[Azure Synapse Analytics]]

**Consulta**

Este servicio acelera la obtencion de información de los sistemas de alamacenamineto de datos.

Se integra con Data Lake, Data Factory, etc

##### [[Azure HD Insights]]

**Procesos**

Hace más fácil, rapido y rentable procesos grandes cantidades de datos, podemos ejecutar Apache y los demas versiones

Se cobra por minuto

##### [[Azure DataBricks]]

**Colaboraciones de datos**

Ayuda a descubrir informaciond de todos los datos y crear soluciones de inteligencia artifical

##### [[Azure Data Lake]]

Este servicio lo que hace es ser un respositorio enorme de datos pero sirve para analizar los datos y hacer un preproceso.

Pueden analizar desde Terabyte hasta Petabytes de datos

Acepta distintos tiposn de lenguajes

Servicios de trabajo de analisis a peticion que simplifican los macrodatos

[[Azure Data Factory]]

Permite colocar un script para poder filtrar los datos y que salga desde una sola fuente, para poder hacer una pagina, una IA.

Convierte los datos en varias fuentes, los limpiamos de cierta manera para poder utilizarlos 

*** ***