# IoT (Internet of Things)

IoT es una red de dispositivos conectados que envía datos a un sistema informático centralizado y que recibe datos de este. La informacion se transmite por internet, se envia a und punto de conexion que procesa y almacena los mensajes. La informacion se recopila por sencsores integrados que mencionaremos mas adelante
 
En otras palabras une el mundo físico y el digital, permitiendo que dispositivos con sensores y una conexión a Internet se comuniquen con sistemas basados en la nube a través de Internet para el análisis de datos.

Los dispositivos inteligentes están equipados con sensores que recopilan datos. Algunos sensores comunes son:

-   Sensores de entorno que capturan los niveles de temperatura y humedad.
-   Escáneres de códigos de barras, códigos QR.
-   Sensores de proximidad y ubicación geográfica.
-   Sensores de luz, color e infrarrojos.
-   Sensores de sonido y ultrasonido.
-   Sensores táctiles y de movimiento.
-   Sensores de inclinación y acelerómetros.
-   Sensores de humo, gas y alcohol.
-   Detectores de errores para determinar cuándo hay un problema con el dispositivo.
-   Sensores mecánicos que detectan anomalías o deformaciones.
-   Sensores de flujo, nivel y presión para medir gases y líquidos.

Con Azure IoT, los dispositivos pueden enviar la informacion a un punto de conexión específico de Azure por medio de un mensaje. Los datos del mensaje se recopilarían y se agregarían y se podrían convertir en informes y alertas. Tambien podriamos acutalizar el frimware o agrega funcionalidade con envio de mensajes con Azure IoT.

Los datos recopilados de estos dispositivos se pueden combinar con servicios de inteligencia artificial de Azure para ayudar a predecir cuando necesitemos realizar algun cambio en nuestro objeto, como el inventario de un alamcen, ampliarlo, arreglarlo, etc.

Los servicios de Azure IoT son los siguientes:

- [[Azure IoT Hub]]
- [[Azure IoT Central]] 
- [[Azure IoT Sphere]]

<h3> Análisis de los criterio de decisión

Que criterios se toman para decidir que servicio de Iot usar de acuerdo con la necesidad empresarial 

<h5> Seguridad

- Es importante  garantizar la integridad de los dispositivos de nuestros clientes para que estos mismo no sean ariesgados y usados de manera malintencionada. Cuando contamos con un dispositivo que es fundamental el uso de seguridad es ideal el uso de Azure Sphere.


- _Conocemos la importancia de Sphere y como este esuna buena opcion para garantizar 
	 la seguridad de comunicación entre el dispositivo y Azure mediante el control de todo (Hardware,S.O, autenticación_

<h5> Informes y Admistración

- Si para nuestro equipo requerimos conectar los dispositivos por medio de telemetría y ocasionalmente actualizar los dispositivos, pero no requerimos de informes podemos optar por Azure IoT Hub 

- En cambio si requerimos una interfaz con la que ver y controlar los dispositivos de forma remota, podemos optar por Iot Central ya que podemos controlar uno o varios dispositovs y configurar alertas para determinadas condiciones.

<br>

**El IoT es una evolución emocionante de la informática que une los mundos físico y digital. Los servicios de Azure IoT proporcionan una gran cantidad de funcionalidad a las organizaciones que quieren compilar soluciones basadas en sensores y dispositivos.**



