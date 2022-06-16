# Azure Defender for Cloud

Defender for Cloud o tambien conocido como security center es un servicio de seguridad e azure que nos permite  visibilidad del nivel de seguridad en todos los servicios, en Azure y el entorno local.


_Nivel de seguridades son las directivas y los controles de ciberseguridad, así como a la predicción, la prevención y la respuesta a las amenazas de seguridad._

Defender Cloud puede hacer lo siguiente:

-  Supervisar la configuración de seguridad en las cargas de trabajo locales y en la nube.

- Aplicar de manera automatica la configuracion de seguridad necesaria a los recursos con los que ya contamos o a los nuevos que se van creando

- Recomendaciones de seguridad

- Supervisa de forma continua los recursos y realiza valoraciones para buscar vulnerabilidades

- Aprendizaje automatio para detectar y bloquear posible malwares en nuestros recursos como MV's

- Usar _controles de aplicaciones adaptables_ para definir reglas que indiquen las aplicaciones permitidas a fin de garantizar que solo se puedan ejecutar las aplicaciones permitidas.

- Detectar y analizar posibles ataques o comandos que se ejecuten de manera extraña

- Control de acceso Just-in-Time a los puertos de red, reduce la superfice expuestaa ataques al garantizare que la red solo permite el trafico que se require

-----------
<h2>Reconocimietno del nivel de seguridad

Con Defender for cloud podemos hacer un analisis deetallado sobre los distintos componetes de nuestro entorno, este analisis se realiza con los controles de sefurida de cualquier directiva de gobernanza que se haya asignado. Podemos ver el cumplimiento normativo desde una perspectiva de seguridad desde una sola ubicacion

-----------
<h2>Protección de seguridad de  recursos

Con **_Protección de seguridad de  recursos_** podemoss ver el estado de los recursos desde el punto de vista de seguridad, asi facilitando que recurso priorizamos para realizar las correciones adecuadads, su clasificaciones de baja, medioa y alta 

_Ejemplo_

![[Pasted image 20220616003412.png]]
-----------
<h2>Puntuación de seguridad

Es una medida del nivel de seguridad de una organización, la puntuación se basa en controles de seguridad o en grupos de recomendaciones de seguridad.La puntuacion es un porcentaje del que tanto se satisfacen las necesidad de seguridad segun los controles de seguridad.

Gracias a la puntuacion podemos mejorar la seguridad para protección contra amenazas, se cuenta con un panel en Defender  para supervisar la seguirdad de nuestrsos recursos, ademas ayuda a:

-   Notificar el estado actual del nivel de seguridad.

-   Mejorar el nivel de seguridad al proporcionar detectabilidad, visibilidad, orientación y control.

-   Comparar con los puntos de referencia y establecer indicadores clave de rendimiento (KPI).

-----------
<h2>Proteccion frente a amenazas

Defender cuenta con defensas para las maquinas virtuales, seguridad de red e integridad de los archivos como las siguientes:

- **Acceso Just-in-Time**

	-  Es un acceso que bloquea el trafico de forma predeterminada en puertos especificos de la maquina virtual pero permite otro trafico durante un tiempo especifico cuando el administrador lo solicita y este lo aprueba. En pocas palabras solo permite el acceso de trafico cuando lo necesitamos antes no pasa na de na.
	
- **Controles de aplicaciones adaptables**

	- Los controles, configuramos que aplicaciones se pueden ejecutar en las maquinas virtuales, ademas se conoce que se ejecuta en la maquina y se pueden recibir recomendaciones. Si se ejecuta una aplicacion no autorizada podemos recibir una alerta.
	
-  **Proteccion de red adapatable**

	- Se realiza un analisis sobre el trafico en las maquinas virtuales para compararlos con los grupos de seguridad y con ello recomendar sobre si los NSG deben bloquearse y proporcionar pasos para corregir 

- ** Supervisión de la integridad de los archivos**

	- Esta funcion sirve para vigilar si hay cambios en archivos importantes, tanto en windows como linux, la congifuracion de los archivos o apps puede ser un ataque

----

<h2> Responder a las alertas 

Para responder a las alertas podemos hacerlo con automatización usando conectores entre [[Azure Logic Apps]] y [[Azure Defender for Cloud]] y asi al detetectar amenazas podemos crear una accion para realizar una defensa.
