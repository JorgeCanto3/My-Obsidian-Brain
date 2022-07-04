# Sesion 10
## Seguridad en la nube
_Pa evitar  el hakin_

En la metodologia de tener un servicio es escencial contar con la confiaza de Zero Trust , "No confíe en nadie, compruébelo todo"

La seguridad en un entorno de nube cuenta con los siguientes pilares:

- Identidades
	- Usuarios y Contraseñas
		- Requerimos que los usuarios cuenten con una buena contraseña para que estos no se vuelvan una vulnerabilidad de nuestro sistema

- Dispositivos (EndPoints)
	- El punto final a donde llegara nuestro servicio, el sevicio esta expuesto a la vulnerabilidades

- Aplicaciones
	- Vulnerabilidades en las aplicaciones, abriendo brechas para descargar o ejecutar codigo

- Tendencias
	- DDos en empresas en fechas importantes por activistas  

- Infraestructura
	- Maquinas virtuales
	- Redes
	- Paginas
	- Todo con lo que contamos desde lo fisico hasta lo digital, (Onpremises) 

- Redes
	- En transito
		- Desde el EndPoint, Proveedor de internet pasando por el  concentrado de internet hasta el data center, se debe proteger por:
		- Cifrado 
		- VPN 
		- etc.

	- En reposo
		- Cuando nuestra inforamacion esta guardada y sin ninguna interaccion o movimiento 
	En ambos casos se deben de proteger la informacion

La seguridad Fisica es muy importante para que no cualquier persona acceda a lo servidores

Sin embargo en el caso de servicios de la nube como PaaS, SaaS o Iaas la seguridad fisica depende de los proveedores del serivicio de nube

La seguriad es por capas y esta es de la siguiente manera:
 -  Seguridad física
	 - Puede protegerse por Azure Sphere
 - Identidad y acceso
	- Usuarios y Contraseña
 - Perímetro
	 - Proveedor de internet
 - Red
	 - Nuestra red
 - Procesos
	 - Enrutamiento,etc. Pueden pasar a nuestra aplicacion
 - Aplicación
	 - Nuestra App, Api,etc
 - Datos 
	 - Datos personales de los usuarios o datos importantes

Con nuestros datos tenemos que mantener tres cosas:
- Confidencialidad
- Integridad
- Disponibilidad



### Microsoft Defender for Cloud
**SaaS**

Podemos ver el nivel de seguridad de los servicios con los que contamos

Es un servicio el cual analiza posibles entradas de ataques

Nos dice como responder antes estos posibles ataques, que  configuraciones de seguridad debemos aplicar e incluso puede aplicar configuraciones de seguridad de manera automatica 

Existen los libros que sirven para ayudarno a hacer investigaciones de seguridad y la configuracion del entorno de la Nube 

Su costo es elevado y cobra por el recurso que se elige para cubrir

**Muestra en el Portal de Azure

### Azure Sentinel
**SaaS**

Nos ayuda detectar posibles fallas o huecos de seguridad y nos ayuda a administrar los eventos de seguridad.

Este sevicio es un SIEM y un SOAR - Seguridad
- Un sistema SIEM recopila los datos de seguridad de todos los recursos, analizarlos y buscar relacion y anomalias entre los datos de analisis. 
	- Administra los eventos de seguridad, nos da informacion junto con lo que esta fallando
- Un SOAR recibe alertas de seguridad y desencadena flujos de trabajo, para actuar y mejorar la seguridad 
	-  Realiza acciones para prevenir o mitigar ataques
- El SIEM le da la info al SOAR 

Investiga amenazas con inteligencia artificial y detecta amenazas que antes no se detectaban

Util para usarla siempreeee



**Log Analytics tiene la informacion de todos los logs de nuestros recursos de azure, registra todo lo que pasa y se lo manda a Centinel**

**_Practica 39:10 _**

### Azure KeyVault 
**SaaS**

Es un almacen de llaves puede administrar nuestros secretos com bien pueden ser claves de cifrado, Certificado SSL . Ademas supervisión y control de acceso.

Tambien puede almacenar nuestros secretos respaldados por modulos de seguridad de hardware HSM

Existen dos tipos de Cifrado:

- Cifrado Simétrico:
	- En este el cifrado solo existe una key, que es compartida para distintos servicios

- Cifrado Asimétrico
	- En este cifrado existen dos keys una publica y una privada, que al momento de usar la publica tiene que ser la misma que la clave privada, la privada nunca se usa. 

- Cifrado consiste en cambiar de posicion los caracteres o el tipo de escritura del lenguaje para que no pueda ser interceptado por ningun hacker, con la llave se descifra para obtener la clave real

### Azure Dedicated Host
**IaaS**

Servidores fisicos dedicados para las virtual machines, aqui se nos da servidores fisicos para nosotros solo. Es util para cumplir la ley debido a que en ciertas regiones necesitamos servidores dedicados con los datos de los usuarios como lo indican las leyes

Se cobra por host dedicado y por hora. Ademas podemos elegir las capacidades del servidor

### Azure Information Protection
**SaaS**

Clasificamos y protegemos documetnos y correos electronicos mediante etiquetas, se clasifica por medio de una inteligencia artificial y esta misma coloca la etiqueta

Se aplican automaticamente la reglas, lo podemos utiliza con el exlporador de windows o el powershell

Util apra proteger datos sensibles

Este servicio aplica limitaciones en los documentos para  que la informacion esten seguros y no se conozca con facilidad


### Microsft Defender for Identity
**SaaS**

Identifica, detectae investiga amenazas, identidades en peligroy acciones internas maliciosas. Este tambien supervisa a los usuario e identifica actividades sospechosas

Se investiga mediante inteligencia artificial para evitar que se conozcan claves de la empresa

Siempre se debe usar en organizaciones medianas o grandes

En pocas palabras nos informa sobre cada accion sospechosa que se realice  

### Network Security Group - Grupo de seguridad de red (NSG)
**IaaS**

Este servicio nos permite filtrar la red de trafico desde y hacia los recusos en redes virtuales. 

Establecemos reglas para filtrar por puerto, direcciones IP o protocolo

Son utilis para poder aislar Maquinas Virtuales y hacer subredes 

**Practica  1:16:00**

### Grupo de seguridad de aplicaciones  - (ASG)
**IaaS**

Crea reglas de seguridad en las maquinas virtuales al mismo tiempo.

Agrupa varias MV con requisitos de filtrado similares, podemos reutilizar las directivas de seguridad.

Con esto podemos aplicar ls reglas de seguridad al mismo tiempo y reducimos esfuerzos en el mantenimiento

#### Diferencia de NSG y ASG

**NSG:**
- Se filtra el tráfico entrante y saliente de las redes virtuales

 **ASG:**
 - Agrupa logicamente las redes virtuales para poder realizar un mantenimiento con menor complejidad
![[ASG.jpg]]

### Azure Firewall
**FaaS**

Permite pasar o niega el trafico según su direccion IP, puede bloquear a un hacker par impedir robo o un ataque

Cone esto protegemos las **Red** ante ataques

Se usa una IP estática para que lo externos se comuniquen

Funciona desde las maquinas hasta el On-Premise

Deniega el trafico de forma predeterminada tanto de entrada como salida, si se llega a meter un hacker, para que nuestra informacion no salga de nuestro servidor

### Azure web application Firewall
**FaaS**

Ayuda a proteger nuestras aplicaciones web, podemos supervisar los ataques y registros. Integrado con Security Server

Es lo mismo que **Azure Firewall** pero para aplicaciones web

![[WAF.jpg]]

### Azure DDoS Protection
**SaaS**

**Todo recurso de azure cuando se crea tiene proteccion ante un ataque DDoS y es gratuito, la version Standar**

Corrige el tráfico no deseado antes de que cause afectaciones

Seguridad perimetral

El nivel basico es habilitado de amnera automatica con este se añade servicios de servicios de mitigacion para las Maquinas Virtuales

![[ddos.jpg]]

Al tener un Servicio de DDoS de paga el ataque lo absorbe Azure