# Azure Sentinel
Azure sentinel es un sistema SIEM, SIEM es un sistema que agrega datis de seguridad de distintos orgienes ademas proporciona detección de amenzas y respuestas ante estas, en la nube de Microsoft se usa una analisis de seguridad inteliegentes y un analisis de amenzas.

Con sentinel podemos realizar lo siguente:

- **Recopilación de datos en la nube a gran escala**
	- Como de usuarios, dispositivos, aplicaciones e infraestructura, local o de distintas nubes
	
- **Detección de amenazas no detectadas anteriormente**
	- Con el analisis y la inteligencia podemos evitar falsos positivos
 
-  **Investigación de amenazas con inteligencia artificia**
	- Con una IA podemos analizar a gran escala 

-   **Respuesta rápida a los incidentes** 
	- Use la orquestación y la automatización de tareas comunes integradas.

----

<h2> Conexion de orígenes de datos

Admite una serie de origenes de datos con los cuales puede realizar analizar en busaca de eventos de seguriad, se administran conectores integrados o API

- **Conexión de soluciones de Microsoft**
	- Los conectores proporcionan integración en tiempo real para servicios como las soluciones de Protección contra amenazas

- **Conexión de otros servicios y soluciones**
	-  Hay conectores disponibles para servicios y soluciones comunes que no son de Microsoft, incluidos AWS CloudTrail, Citrix Analytics, etc

-**Conexión de orígenes de datos estándar del sector**
	-Admite datos de otros origenes que usan el estandar de mensajería Formato de evento común (CEF), Syslog o la API REST

----

<h2> Detectar amenazas

Para detectar amenazas podemos usar:

- Análisis Integrado
	- En el análisis integrado usamos plantillas diseñadas por expertos de seguridad. Buscan cualquier actividad que parezca sospechosa en el entorno, en algunas se utiliza el análisis de comportamineto de aprendizaje automático que se basa en algoritmos.

- Análisis personalizado 
	- Aqui el análisi son reglas que se crean para buscar criterios concretos en el entorno, podemos obtener una vista previa de la consulta y una programación para que se ejecute la consulta, ade mas de establecer un umbral de alertas.

----

<h2> Investigacion y respuesta

Con la invstigacion podemos revisar la infromación de entidades directamente conectadas a la alerta y ver consultas de exploración comunes para ayudar a guiar la investigación.

_Ejemplo_

![[Pasted image 20220616014012.png]]

Cuando un administrador selecciona **Bloquear**, la dirección IP se bloquea en el firewall y el usuario se deshabilita en Azure Active Directory.

Cuando un administrador selecciona **Omitir**, la alerta se cierra en Azure Sentinel y el incidente se cierra en el sistema de incidencias de TI.