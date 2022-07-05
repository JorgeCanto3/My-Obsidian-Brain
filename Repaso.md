# Azure IoT
 Iot nos permite a nuestros dispositivos recopilar y transmitir la informacion para analizarla. En si se puede concetar cualquier dispositivo inteligente que cuente con sensores para poder recoplar datos.

 Azure Iot nos permite conectar los dispositivos con sensore y con conexion a internet para poder enviar los datos a azure por medio de un mensaje, para despues poder recopilarlos y hacer informes y crear alertas con esto podemos controlar, administrar y proteger los dispositivos, ademas de crear soluciones.
 
  Azurecuenta con 3 sistemas principales para poder concetar nuestros dispositivos 
  
  - **Azure Iot Hub**
	  - Con este servicio podemos conectar los dispositovs a Azure desde la consola, esta hospedado en la nube y actua como centro de mensajes, la comunicacion es bidireccional. 
	  - Su comunicacion puede ser nube a dispositivo o dispositivo a nube
	  - Permite ordenar y controlar. Podemos tener control remoto manual o automatizado de los dispositivos

  - Azure Iot Central
	  - En pocas palabras con Central podemos hacer lo Mismo que con Hub pero en central existe un panel con el podemos interactuar y realizar las tareas con más facilidad pero teniendo limitaciones. Con la interfaz grafica el uso es más claro, ademas de que se cuentan con Plantillas para poder configurar distintos escenarios

  - Azure Sphere
	  -  Es una solucion de IoT para poder darle seguridad a los dispositivos conectados, de extremo a extremo, proporciona seguridad desde el Sistema operativo hastra el hardware para hacer seguro el envio de mensajes al centro de mensajes

	- Consta de 3 partes
		- Un microcontrolador para poder procesar e sistema operativo y las señales de los sensores conectados
		- S.O de linux que controla la comunicacion
		- AS3 se asegura de que el dispositivo no se ha puesto en peligro de forma malintencionada

# Seguridad en Azure
Azure cuenta con diversos servicios de seguridad para poder cuidar de nuestros recursos y cumplir con un minimo nivel de seguridad y poder protegerlos ante atraques

La seguridad de mide por capas de profuncidad 

Esta capas se organizan de la siguiente manera

![[Pasted image 20220704184131.png]]
Aquí tiene una breve descripción del rol de cada capa:

-   La capa de _seguridad física_ es la primera línea de defensa para proteger el hardware informático del centro de datos.
-   La capa de _identidad y acceso_ controla el acceso a la infraestructura y al control de cambios.
-   La capa _perimetral_ usa protección frente a ataques de denegación de servicio distribuido (DDoS) para filtrar los ataques a gran escala antes de que puedan causar una denegación de servicio para los usuarios.
-   La capa de _red_ limita la comunicación entre los recursos a través de controles de acceso y segmentación.
-   La capa de _proceso_ protege el acceso a las máquinas virtuales.
-   La capa de _aplicación_ ayuda a garantizar que las aplicaciones sean seguras y estén libres de vulnerabilidades de seguridad.
-   La capa de _datos_ controla el acceso a los datos empresariales y de clientes que es necesario proteger.

### Libros
Los libros sirven para poder hacer investigaciones de seguridad y podemos hacer pequeñas configuraciones de seguridad, en Sentinel podemos supervisar más fácil los datos conectados

## Azure Security Center o Microsoft Defender for Cloud
**Niveles de servicio**

Con este servicio podemos hacer una supervision de los niveles de seguridad de los servicios de Azure, así como los de nuestro entorno local.

**_Nivel de seguridad_** 
- Este termino ahce referencia a las directiva con las que contamos, los controles de ciberseguridad, ademas de la prediccion, prevención y la respuesta ante amenzas  


Puede 
- **supervisar las configuracion de seguridad en la nube y local**
- **aplicar una configuraciona automatica** segun se necesite
-  Da **recomendaciones de seguridad** segun las configuraciones
-  Supervisa los recursos para identificar **posibles vulnerabilidades antes de que se usen**
- **Aprendizaje automatico** para detectar y bloquear malware de las MV's
- **Detectar y analizar posibles amenzas** entrantes e investigar amenazas posterior a una brecha
- **Control de Acceso Just-in-Time** a los puertos de red


Ademas de lo anterior mencionado se nos puede proporcionar un reconocimiento del nivel de seguridad o bien una puntuacion de la seguridad general
![[Pasted image 20220629023008.png]]

**La puntuacion de seguridad** 
- Es una mediad del nivel de seguridad de una organizacion, esta se basa en los controles de seguridad, el porcentaje que se da se basa en los controles de seguridad que se satisfacen. Podemos corregir errores y aumentar la puntuacion
- ![[Pasted image 20220629023503.png]]

Existe un apartado de proteccion de seguridad recursos con el cual podemos ver el estado de sus recursos en cueestion seguridad. Nos dara acciones corrctivas que se clasifican en graveda, baja, media y alta

![[Pasted image 20220629023241.png]]


Para la proteccion ante amenazas se ofrece:
- **Acceso Just in Time**
- **Controles de aplicaciones adaptables**
	- Q apps se pueden ejecutar en las maquinas virtuales
-  **Protección de red adaptable**
	-  Supervisa el trafico 
- **Supervisión de la integridad de los archivos**

Por ultimo podemos crear una _automatización de flujo de trabajo_ para responder antes cierta alerta o amenaza.

---------
## Azure Sentinel
### Conceptos del Tema
- **SIEM**
	- este sistema agrega datos de seguridad de muchos origenes distintos (Siempre y cuando se adminta un formato de registro)
	- Recopila los datos de seguridad de todo como los serivicios, infraestructura, etc y los analiza para poder detectar anomalias o relaciones
- **SOAR**
	- Recibe alertas de seguridad de distintos origeenes pero principalmente desencadena flujos de trabajo dependiendo de las interacciones de los usuarios.
		- Como ingresar a la plataforma y limitar ciertos accesos
	- En otras palabras actua ante una posible amenza
	
--------
### Definicion 

Azure sentinel es otro servicio de seguridad que es el sistema  SIEM basado en la nube de Microsoft, tambien utiliza el sistema SOAR

Este servicio funciona con todos los datos de nuestra nube, tambien esta conectado con Azure monitor para saber el estado de los recursos y sabes si alguno esta fallando

Con Sentinel podemos:

- **Recopilación de datos en la nube a gran escala**
	- Recopla todos los datos de los usuarios, dispositivos, apps, infraestructura local y de la nube
- **Detección de amenazas no detectadas anteriormente**
- **Investigación de amenazas con inteligencia artificial**
- **Respuesta rápida a los incidentes**
	- SOAR
- 

**Conexion de Datos**

Sentinel Admite distintos conexiones de datos para poder analizarlos en busca de un evento de seguridad, son administradas por concetores integrados o API y formatos de registro estándar:

- **Conexión de soluciones de Microsoft**
- **Conexión de otros servicios y soluciones**
- **Conexión de orígenes de datos estándar del sector**

**Detectar Amenazas**

Para poder detectar amenazas podemos utilizar dos tipos de análisis:

- Análisis Integrado
	- Este analisis esta prediseñado con plantillas ante amenazas ya conocidas, ademas estan realizadas por expertos y se pueden personalizar a las sospechas o analisis que querramos hacer.
- Análisis Personalizado
	- En este analisis contiene reglas para buscar criterios en nuestro entorno

**Investigación y respuesta** 

Al recibir una alerta de un evento sospechoso podemos investigar las alertas o incidentes. con un grafico que nos proporciona, informacion de las entidades

![[Pasted image 20220629210906.png]]

La empresa también usará Libros de Azure Monitor para automatizar las respuestas a las amenazas

## Azure Key Vault

Key Vaul es un servicio que nos permite guardar los secretos de nuestras aplicaciones. Proporcona un acceso seguro y confidenciial a la infromacion mediante los controles de acceso y registro

Puede: 
- **Administrar secretos **
	- Guarda de forma segura y controla el acceso a tokens, contraseñas, certificados o claves API
- **Administración de claves de cifrado**
	- facilita la creación y el control de las claves de cifrado que se emplean para cifrar los datos.
- **Administración de certificados SSL/TLS**
- **Almacenamiento de secretos basado en módulos de seguridad de hardware(HSMs)**
	- Se pueden proteger las claves con software o HSM en la version premium

![[Pasted image 20220629215457.png]]


Las ventajas de Key vault es que es centralizado y asi se distribuyen menos, se almacenan de manera segura, podemos supervisar los accesos ademas de que lo podemos integrar a otros servicios de azure


## Azure Information Protection

Azure Information Protection (AIP) es una solución basada en la nube que permite a las organizaciones descubrir, clasificar y proteger documentos y correos electrónicos mediante la aplicación de etiquetas al contenido.

![[Pasted image 20220702221834.png]]


## Azure Dedicated Host
Nos proporciona servidores físicos dedicados para hospedar las maquinas virtuales de Azure para Windows y Linux, con estos podemos cumplir normas que obliguen a ser el unico cliente que use el equipo 

![[Pasted image 20220702232042.png]]

A un host dedicadose le asigna un servidor físico en un centro de datos de Azure, un grupo de datos es una coleccion de host dedicados

Podemos: 
- Observar y controlar la infraestructura del servidor de Azure
- Podemos poner cargas de trabajo en un servidor Aislado
- Podemos elegir 
	- Los procesadores
	- Las capacidades del servidor
	- Las series de MV's
	- El tamaño ded la maquina virtual dentro del mismo host

Con el _grupo de hosts_  podemos lograr una alta disponibilidad e implementar las maquinas virtuales

El precio de este serivicio es por host, se basa en la region , la familia de MV's y El tipo de hardware

## Azure Firewall
Es un servicio de seguridad de red administrado y basado en la nube que ayuda a proteger los recursos y las redes virtuales de azure

Un **firewall**es un dispositivo de seguridad de red que supervisa el tráfico de red entrante y salieente y decide si se permite o se bloque un trafico especifico en funcion a un conjunto definido de reglas de seguridad, podemos especioficar intervalos de direcciones IP, solo ciertas IP's podran accesar

![[Pasted image 20220704185812.png]]

A. Firewall tiene estado, este estado analiza el contexto completo de una conexion de red y no solo su paquete individual de tráfico de red

Incluye alta disponibilidad y escalabilidad en la nube sin restricciones 

Proporciona una ubicación central para crear, aplicar y registrar directivas de conectividad de red y de aplicaciones entre suscripciones y redes virtuales. Azure Firewall usa una IP invaribale o estatica para las redes virtuales para que asi los firewall extereno identifiquen una red virtual entrante, se integra con Monitor

Cuenta con:

- Alta disponilidad integrada y la escalibilidad SI
- Reglas de filtrado del trafico entrante y salienet
- Traduccion de direcciones de destino ( DNAT)
- Registo en Monitor

Firewall implementa una red central para poder controlar el acceso general a la red

Podemos configurar:

-  Reglas de aplicacion 
	- Que definene nombres de dominio completos, a estos podemos acceder desde una subred
- Reglas de red
	- Definen la direccion de origen, protocolo, el puerto y la direccion de destino 
- Reglas de traducción de direcciones de red (NAT)
	- Definen los puertod y las direcciones IP de destinos para traducir las solicituddes entrantes

Azure App Gateway es un firewall de aplicaciones web (WAF), proporcviona proteccion centralizada para las aplicaciones web contra las vulnerabilidades de seguridad comunes
# Azure Virtual Networks

Las redes virtuales de Azure permite a los recursos de Azure conectarse entre si, puede considerado una extension de la red local con recursos que vincula otros recursos de Azure

- Las redes virtuales cuentan con las siguientes funcionalidades:

	- **Aislamiento  y segmentación**
		- Podemos definir un espacio de direcciones IP privada con intervalos de IP publicas o privadas, el publico solo existe en la red virtual. Este espacio lo podemos dividir en subredes y en ese espacio definimos cada subred
	- **Comunicación con Internet**
		- Podemos habilitar las conexiones de intetnet en una maquina virtual asignando una IP pública a la maquina virtual
	- **Comunicación entre recursos de Azure **
		- Podemos comunicar a los recursos con dos metodos:
			- Redes Virtuales
				- Podemos conectar distintos recursos de Azure
			- Puntos de conexión de servicio
				- Tambien podemos conectar distintos recursos de azure pero podemos mejorar la seguridad y proporcionar un enrutamineto optimo entre los recursos
	- **Comunicación con los recursos locales**
		- Podemos vincular los recursos locales entre si con la suscripcion de tres maneras:
			- **Redes privadas virtuales de punto a sitio**
				- El equipo cliente inicia una conexión VPN cifrada para conectar ese equipo a la red virtual de Azure.
			- **Redes virtuales privadas de sitio a sitio**
				- Vincula un dispositivo o puerta de enlace de VPN local con la puerta de enlace de VPN de Azure en una red virtual.
			- **Azure ExpressRoute**
				- Proporciona una conectividad privada dedicada a Azure que no viaja por Internet
	- **Enruamiento del trafico de red**
		- Azure enruta de forma predeterminada el trafico entre sub redes de todas las redes. para controlarlo podemos hacer lo siguiente
			- **Tablas de rutas**
				- Define las reglas para dirigir el tráfico y cvon estas podemos controlar como se enrutan los paquetes en las subredes
			- **Protocolo de puerta de enlace**
				-  Propaga las rutas BGP locales a las redes virtuales de azure, este funcina con las puertas de enlace de VPN , Route server o Express route
	- **Filtrado del tráfico de red**
		- Podemos filtrar el trafico de red  con los siguientes metodos
			- **Grupos de seguridad de red(NSG)**
				- Es un recurso de azure con el cual podemos crear reglas para la seguridad de entrada y salida, podemos bloquar  o permitir el trafico de acuerdo al puerto, IP, origen y destino.
			- **Aplicaciones virtuales de red**
					- Es un MV especializada que ejerce una funcion de red determinada, como ejecitar un firewall o optimizar la red 
	- **Conexión de redes virtuales**
		- Podemos vincualr llas redes virtuales con el emparejamiento, permitiendo que los recursos de cada red se comuniuen entre si. Si las redes son de distintas regiones podemos crear una red global interconectada
		- Las rutas definidas por el usuario permiten un mayor control sobre el flujo de tráfico de red, 

![[Pasted image 20220703213355.png]]

Al crear una red virtual podemos 
- Definir el espacio de direcciones
- La subred
- Los puntos de conexion
- Puerta de enlace 
- Habilitar BastionHost
- Habilitar DDos protection
- Habilitar Azure Firewall

## Azure VPN Gateway

Las VPN's son un túnel cifrado en otra red, se utilizan para conectatr entre sí dos o más redes privadas de confiaza usando una que no lo es, la informacion se cifra pera evitar ataques o que la informaicon sea interceptad

### Puertas de enlace de vpn

Una puerta de enlace es un tipo de puerta de enlace de red virtual. VPN gatewat tiene una subred para la conectividad que permite 

- Conexion de sitio a sitio 
	- Centros de datos locales a redes virtuales
- Conexion de punto a sitio
	- Dispositivos individuales a redes virtuales
- Conexion de entre redes
	- Las redes virtuales a otras redes virtuales

![[Pasted image 20220703224612.png]]

Con las puertas de enlace se pueden usar par conectarse a varias ubicaciones como otras redes virutales o centros de datos locales

### Redes virtuales Basadas

Al implementar una instancia tenemos que especificar el tipo de red virtual basada

- Directivas
	- Tenemos que especificar de forma estatica la direccion IP de lo que se va a cifrar a través de cada tunel 
- Rutas
	- Los tuneles IPSec se modelanncomo una interfaz de red, cuando se enrutan se decide en que tunel se va a enviar cada paquete


### Recursos necesarios

Antes de implementar VPN Gateway necesitamos
- Red Virtual 
- GatewaySubnet
- Direccion IP pública
- Puertra de enlace de red local
- Puertra de enlace de red virtual
- Conexion 

![[Pasted image 20220703225746.png]]


### Escenarios de alta disponibilida
Para tolerancia a errores

#### Activo-en espera
Con este hay alguna interrupcion la instancia en espera asime de forma automatica la responsabilidad de conexiones sin que el usuario intervenga, si se interrumpe normalmente se recupera al poco tiempo si es mantenimiento es un plazo de 90 sg

![[Pasted image 20220703230317.png]]
#### Activo/activo

se asigna una IP pública única a cada instancia. Después, se crean túneles independientes desde el dispositivo local a cada dirección IP.

![[Pasted image 20220703230415.png]]

## Azure ExpressRoute
**Es una conectividad PRIVADA pero no se encuentra CIFRADA**

Con expressroute podemos establecer una conexion a la nube de microsoft, ampliando las redes locales y conectandonos a servicios como Azure o Microsof 365. 

Esta conexion puede ser por una IP VPN, ethernet (Punto a Punto), adicional las conexiones no pasan por una red publica como el internet haciendo que sea más segura, teniendo mayor velocidad y menor latencia 
![[Pasted image 20220703232320.png]]

### Caracteristicas  y ventajas
Las ventajas son las siguietnes

- Conectividad Nivel 3 ente la red local y Microsoft Cloud mediante un proveedor de conectividad
- Conexion a los servicios de la nube de Microsoft en todas las regiones dentro de la geopolitica 
	- A todos los servicios de microsoft pero con ExpressRoute Premium
- Enrutamiento dinámico entre la red y microsoft con BGP ( Puera de enlace borde)
	- Intercambiuo de rutas entre la red local y los recursos de Azure
- Redundancia integrada
	- Garantizar que las conexiones establecidas con Microsoft tengan alta disponibilidad.
- SLA

### Conectividad de ExpressRoute

Existen tres distinto modos de conectar la red local con la nube

![[Pasted image 20220703233209.png]]
# SLA y Ciclo de vida del servicio
El SLA es el Service Level Agrement o Acuerdo de nivel de servicio es un contrato formal entre una empresa de servicio y el cliente,en el caso de Azure aqui se definen los estandares de rendimiento que se le proporcionara al cliente.

Son realmente importantes ya que nos ayudartan a conocer la disponibilidad de los servicios y su rendimiento 

_Los servicios gratuitos no tienen SLA_

**Aspectos que incluye  un acuerdo de Nivel de Servicio típico**

- Introduccion
	-  Se explica que esperar del SLA
- Terminos generales
	- Contiene los terminos del SLA para que el cliente y microsoft entiendan y compartan el mismo vocabulario
-  Detalles del SLA
	- Se definen las garantias especificas del servicios
		- Normalmente estan comprendidos en 99.9% o 99.99%

## Porecetnajes y tiempo de inactividad total

El tiempo de inactividad es cuando el servicio no esta disponible.

La diferncia de .99 a .9999 es grande por ello es importante conocer la diferencia 
![[SLA 99.jpg]]

## Creditos de servicio
Los creditos son el procentaje del precio que se ha pagado que se nos regresara con forme reclamemos por los fallos

Para solicitar los creditos tenemos que mandar una reclamacion  de acuerdo al SLA que nos indicara cuando enviar la reclamacion
## Interrupción en el servicio

Par conocer alguna interrupcion de un servicio lo podemos ver desde [Estado de Azure](https://status.azure.com/status) donde nos da una vision global de los servicios y regiones

## SLA App
Un _acuerdo de nivel de servicio de la aplicación_ define los requisitos del acuerdo para una aplicación específica. Este término normalmente hace referencia a una aplicación que el _cliente_ compila en Azure.

Es el SLA que le ponemos a nuestra aplicacion de acuerdo a lo que contamos, para ello debemos identifacar las cargas de trabajo, es una función o tares distinta que se separa de las más, Cada carga define un conjunto de requisitos para la disponibilidad, la escalabilidad, la coherencia de los datos y la recuperación ante desastres.

El proceso de combinación de acuerdos de nivel de servicio ayuda a calcular el _acuerdo de nivel de servicio compuesto_ para un conjunto de servicios. Para calcular el acuerdo de nivel de servicio compuesto, hay que multiplicar el acuerdo de cada uno de los servicios.
![[SLA compuesto.jpg]]

Combinarlos da como resultado un número total que es _inferior_ al 99,9 % que necesita. Porque el uso de varios servicios agrega un nivel de complejidad adicional y aumenta ligeramente el riesgo de que se produzcan errores.

Si implementamos dos o más instancias de una máquina virtual en las diferentes zonas de disponibilidad de una misma región de Azure eleva el SLA del servicio. Ademas para garantizar la alta disponibilidad podemos aplicar la redundancia que es el duplicado de componentes en varias regiones. Si queremos refucir costos podemos simplemente ejecutarlo en una sola región 

La redundancia incluyela propia aplicación, así como los servicios y la infraestructura subyacentes, este servicio es dificil y caro solo utilizarlo de ser necesario


## Ciclo de vida de un servicio
Es la forma en que cada servicio de Azure se pone a disposición del público.

Todos los servicios de Azure comienzan en:
- **La fase de desarrollo**
	- Aqui se recopila, definen los requisitos y comienza la creacion del serivicio
- Luego sigue la **Fase de versión preliminar pública*
	-  El publico puede acceder al servicio experimentar con el, ademas de poder proporcionar ocmentario reales para poder mejorar el servicio y poder solicitar nuevas funcionalidades o distintas 
-  Una vez validado se pone a disposicion a todos los clientes como servicio listo para la produccion se le conoce como **Disponibilidad General** (GA)

Cada version preliminar define sus terminos y condiciones

#### Acceso
Podemos acceder a ellos desde el portal de azure 

Podemos acceder a las nuevas caractersticas en su version preliminar de un servicio estan disponibles al implementar, configurar y administrar el servicio

#### Portal
Existen veriones preliminares que son para el porrtan a las cuales podemos acceder en  [Microsoft Azure (versión preliminar)](https://preview.portal.azure.com/). Estas versiones preliminares ofrecen mejoras de rendimiento, navegacion y accesibilidad a  la interfaz del portal

Podemos distinguir cuando estamos en la version preliminar porque en el encabezado se nos mostrara el siguiente texto
![[Pasted image 20220704163615.png]]

#### Actualizaciones
Para conocer las ultimas novedades podemos checar continuamente la pagina  [Actualizaciones de Azure](https://azure.microsoft.com/updates)

Aqui encontraremos las ultimas actualizaciones de procutos, servicios y caracteristicas de azure y anuncios. Podremos ver los detalles de las actualizaciones y poder ver en que fase se encuentran

# Storage 
Para poder empezar a utilizar los servicios de storagre tenemos que crear una cuenta de almacenamiento y tendremos servcicios como 
- Azure Blob
- Azure Disk
- Azure Files

Con la cuenta podemos accesar desde cualquier lugar al storage através de HTTP o HTTPS. los datos se encuentran seguros, de alta disponibilidad y escalables.
Admite hasta 32 TB

Diagram de como se usa una cuenta de Azure Storage

![[Pasted image 20220704214953.png]]
## Azure Disk Storage
Proporciona Discos para las maquinas virtuales, al igual a los servicios que lo requieran. Permite que los datos se alamacenen de forma persistente y que se acceda a elllos desde un disco duro virtual conectado

Existen diferentes discos, de distintos tamaños y rendiminetos 

- SSD y HDD para cargas de trabajo m,enos ciriticas 
- SDD premium  para aplicaciones de producción criticas
- Ultra Disks para cargas de trabajo itensos
![[Pasted image 20220704213551.png]]

## Azure Blob Storage
**Blob*
- Un blob (Binary Large Object) son elementos utilizados en las bses de datos para almacenar los datos de gran tamaño que cambian de forma dinámica
	- Suelen ser 
		- Imagenes
		- Archivos de sonidos
		- Objetos multimedia
	- Se almcenan como codigo de binarios Blob


**Descripcion**
Puede almacenar grandes cantidades de datos como datos de texto o binarios, es un sistema no estructurado, por ende no tenemos restriccion de que tipo de datos almacenar. Puede tener miles de cargas simultaneas, cantidades de datos de video enormes, etc. Podemos acceder a el desde cualquier lugar con internet. 

No se limita formatos de archivos comunes, puede contener gb entero de datos binarios, transmitir datos, mensajes cifrados. El ventaja del servicio  es que no requiere que los desarrolladores lo administren, ya que se cargan como bolbs y azure se encarga de los almacenamiento fisico

## Azure Files

Ofrece la posibilidad de poder compartir archivos totalmente administrados en la nube a los que se pueden acceder meidante protocoles del bloque de mensaje. Se pueden monatar simultáneamente en implementaciones de windows, linux y macOS en la nube o local.

Cualquier número de roles o máquinas virtuales de Azure puede montar y acceder simultáneamente al recurso compartido de almacenamiento de archivos.

En reposo los datos se cifran y el protocolo SMB garantiza que los datos se cifren en tránsito

![[Pasted image 20220704215750.png]]

_Uso de Azure files para compartir dasrtos entre dos ubicaciones geograficas_
Niveles de acceso 

-   **Nivel de acceso frecuente**: optimizado para almacenar datos a los que se accede con frecuencia (por ejemplo, imágenes para el sitio web).
-   **Nivel de acceso esporádico**: optimizado para datos a los que se accede con poca frecuencia y que se almacenan al menos durante 30 días (por ejemplo, las facturas de los clientes).

-   **Nivel de acceso de archivo**: conveniente para datos a los que raramente se accede y que se almacenan durante al menos 180 días con requisitos de latencia flexibles (por ejemplo, copias de seguridad a largo plazo).

# Privacidad
## Declaracion de privacidad 
La declaracion de privacidad de Microsoft Explica que datos personales recopila Microsoft, cómo los usa y con que fines. Abarca todos los servicios de microsoft 

## Terminos de los servicios en Línea

Los termino son un contrato legal entre microsoft y el cliente, en el cual se datallan las obliugaciones de ambas partes con respectos al procesamineto y seguridad de los datos ded los clientes  y los datos personales. Estos terminos se aplican a los servicios en línea de Microsoft


## Anexo de proteccion de datos (DPA)

En el DPA se definen los terminos de seguridad y procesamiento de datos para los servicios en linea como: 

 -  Cumplimiento de leyes
 -  Revelacion de datos procesados
 -  Seguridad de los datos 
 -  Transferencia de datos, retencion y eliminacion 

## Centro de confianza

El centro de confianza es  donde se presenta los principios de Microsoft para mantener la integridad de los datos en la nube y la manera en que microsoft implementa y admite la seguridad, la privacidad, el cumplimiento y la transparencia en todos los servicios.

Nos da:
- Informacioon detallada de la seguridad
- Recursos adicionales a cada tema 
- Vinculos a blogs de seguridad

## Documentacion de cumplimietno de Azure

Esta documentacion nos proporciona documentación detallada sobre el cumplimiento y los estandares legales y normativos en Azure

Existen diversas oferta de cumplimiento en lsa categorias como las siguientes:

- Global
- Gobierno de EE.UU.
- Servicios financieros
- Sanidad
- Soporte físico y fabricación
- Regional




Costos
Cuando se excede el precio de un servicio podemos usar las alertas para conocer el limite
Fase anterior a la GA en el ciclo de vida de un servicio de Azure

**Fases de adopcion de nube
# Gobernanza en la nube
## Acceso a los recursos en la nube por medio del control de acceso basado en roles de Azure (RBAC)

El acceso basado en roles es un buena practica de seguridad ya que unicamente concedemos acceso a los usuarios solo a lo que necesiten. Asi solo colocamos los roles a ciertos usuario en lugar de hacerlo de manera individual.

El acceso basado en roles se aplica a un ambito, un ambito es un recurso o conjunto de recursos en lo que se permite acceso

_Roles y ambitos_
![[Pasted image 20220704221654.png]]

Podemos crear roles que den acceso primario y hereden acceso a los ambitos secundarios

-  Propietario 
	- El usuario podrá administrar todo el contenido de todas las suscripciones dentro de ese grupo de administración.
-   Lector
	- Podrán ver todos los grupos de recursos y recursos dentro de esa suscripción.
-  Colaborador 
	- Podrá administrar los recursos de cualquier tipo dentro de ese grupo de recursos específico, pero no los otros grupos de recursos dentro de esa suscripción.

Podemos aplicar los roles a un grupo o a un solo individuo. Administramos los permisos desde el panel de **Control de acceso(IAM)** del portal de azure, nos muestra los roles y a que ambito se aplican
![[Pasted image 20220704223539.png]]


## Bloqueos

Podemor poner bloqueos a los recursos para protegerlos de incidentes, los bloqueos los administramos desde el portal, PowerShell, el CLI o una plantilla de resource manager como:

-   **CanNotDelete** pueden seguir leyendo y modificando un recurso, pero no eliminarlo sin quitar primero el bloqueo.
-   **ReadOnly** significa que las personas autorizadas pueden leer un recurso, pero no eliminarlo ni cambiarlo. 

Para modificar o cambiar un recurso tenemos que quitar el bloqueo  

Un recurso puede tener multiples bloqueos, heredarlos y agregarlos cuando ya hay uno


## Etiquetas 
 Las _etiquetas_ de recursos son otra forma de organizar recursos. Las etiquetas proporcionan información extra, o metadatos, sobre los recursos.
 
Podemos agregar, modificar o eliminar etiquetas de recursos a través de PowerShell, la CLI de Azure, plantillas de Azure Resource Manager, la API REST o Azure Portal y por Azure policy

## Azure Policy
Es un servicio de Azure que permite crear, asignar y administrar directivas que controlan o auditan recursos. Dichas directivas aplican distintas reglas en todas las configuraciones de los recursos para que esas configuraciones sigan cumpliendo con los estándares corporativos.

para crear una directiva expresa qué se debe evaluar y qué acción realizar para depues debemos asignar definiciones a los recursos.

Tambien existen las iniciativas que es una forma de agrupar directivas relacionadas, estas las definimos por medio del portal o el CLI. 

En un plano tecnico o blueprint se agrupan iniciativas y dentro del plano tecnico cada componente de la definicion se denomina Artefacto

![[Pasted image 20220704225450.png]]

## Cloud Adoption Framework

Es una guia para ayuda la adopcion de la nube, podemos crear e implementar estragias empresariales y tecnologicas para usar bien la nube. 

Adoption incluye las siguientes fases
1.  Definir la estrategia.
2.  Crear un plan.
3.  Preparar la organización.
4.  Adoptar la nube.
5.  Controlar y administrar los entornos de nube.

![[Pasted image 20220704225802.png]]

## Grupos de administracion 

Los grupos de administración también están disponibles para ayudar a administrar las suscripciones. Un grupo de administración se encarga de administrar el acceso, las directivas y el cumplimiento en varias suscripciones de Azure. Nos adentraremos en los grupos de administración más adelante en este módulo.****

## Facturación

Se puede crear un informe de facturación por suscripción. Las etiquetas de recursos también pueden ser de ayuda

Las etiquetas proporcionan información extra, o metadatos, sobre los recursos. Así, el equipo podría crear una etiqueta llamada **DeptFactur** cuyo valor sería el nombre del departamento de facturación. Se puede usar Azure Policy para garantizar que se asignan las etiquetas adecuadas cuando se aprovisionen recursos.


## Control de acceso

Cada suscripción está asociada a un inquilino de Azure Active Directory. Cada inquilino proporciona a los administradores la capacidad de configurar un acceso granular a través de roles definidos por medio del control de acceso basado en roles de Azure.



# Preguntas de examen

Tolerancia a fallos es la capacidad del sistema a continuar en caso de una falla

ISO International organization for Standardization define los estandares minimos 

_La recuperación ante desastres_ es el proceso de restauración de la funcionalidad de la aplicación tras una pérdida catastrófica.

despues de crear un mv necesitamos modificar el nsg para admitir conexiones del puerto 8000

Un servicio de azure esta disponible a todos los clientes cuando esta en la version **publica preliminar**

Para recibir tokens de seguridad Azure AD

Para que una maquina sea accesible por Http e internet modificamos el Azure Firewall

Azure Application Insights Monitorea las aplicaciones web, detecta y diagnostica anomalias en la app

Para recibir apoyo dee ingenieros debemos contar con planes premier o profesionales

El soporte premier es solo para empresas con el acuerdo enterprise (EA)

cualquier suscripcion puede tener apoyo de MSDN

Con monitor podemos monitorear recursos de distintas suscripciones, ver los logs con Azure AD y crear alertas

Para evitar la creacion de un recurso en un grupo de recursos podemos utilizar Azure Policy

Para controlar los puertos NSG

En las suscripciones premier, professional, standar y developer  podemos hacer un peticion de ayuda en los serivicos basicos no

El plan premier ofrece soperte especifico de arquitectura

Todos los servicios con version preliminar son excluidos del SLA

Se cobra por IP's publicas

Informacion almacenada en storage se almacena automanticamnete en al menos tres copia

La informacion no es copiada automaticamente a otro data center

Azure storage 2tb y 1 millon dee archivos = no

La tolerancia a fallos es cuando el servicio sigue a pesar de un fallo

La recuperacion ante desastres es cuando podemos recuperar un servicio despues de un fallo

La escalbilidad dinamica es cundo un servicio se adapta rapidamente cuando hay demanda

Cuando se puede acceder a un servicio rapidamente desde internet se le conoce como baja latencia

Con infroamtion protection podemos protegere los documentos, encrypta o cifrra documento y emails

Azure databrick jala con apache
