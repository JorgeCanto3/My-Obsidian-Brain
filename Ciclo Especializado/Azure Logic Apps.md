<h1>Azure Logic Apps
----------
--------------
<h2>Descripcion
-
-----------------
Modelo de servicio: PaaS, [[Aplicaciones Logicas]]

Es una plataforma de desarrollo de poco código o sin código hospedada como un servicio en la nube. El servicio le ayuda a automatizar y organizar tareas, procesos empresariales y flujos de trabajo cuando tiene que integrar aplicaciones, datos, sistemas y servicios en empresas u organizaciones.

Se simplifica el diseño y las soluciones escalables en la nube o entorno local.

Al igual que functions el uso de este servicio se cobra por evento y el tamaño del mismo, practicamente identico a Functions  pero con entorno virtual

Se diferencia de Functions que logic Apps es visual y todo el tiempo se esta ejecutando

--------
Estado 

Functions:Sin estado pero Durable Functions proporciona el estado

Logic Apps: Functions proporciona el estado.

-----------

Desarrollo

Functions: Orientado al codigo (Imperativo)

Logic Apps: Orietnado al diseñador (Declarativo)

---------------


Conectividad 

Functions: Alrededor de  una docena de tipos de enlaces integrados

Logic Apps: Gran coleccíon de conectores. Creacion de conectores personalizados

---------------

Acciones

Functions: Cada actividad es una función de Azure. Escritura de código para las funciones de actividad.

Logic Apps: Gran colección de acciones listas para usar.

---------------

Supervisión 

Functions: Azure application Insights

Logic Apps: Azure Portal. Log Analytics

---------------
Administracion 

Functions: API REST, Visual Studio.

Logic Apps: Azure Portal, API REST, PowerShell, Visual Studio.

---------------
Contexto de ejecución

Functions: Nube o de manera local

Logic Apps: Nube

---------------
<h2>Caracteristicas
-
--------------
En Azure L.A. comienza con un desencadenador, que se desencadena cuando se prduce un evento especifico o cuando hay nuevos datos disponibles que cumplen determinados criterios 

Algunos desencadenadores incluyen funcionalidades de programación básicas que permiten a los desarrolladorees especificar con que frecuencia se ejecutara las cargas de trabajo

Cada ves que el desencadenador se activa, el motor de Logic Apps crea una instancia de aplicación lógica que ejecuta las acciones del flujo de trabajo. Algunas de las acciones pueden ser incluir conversiones de datos y controles de flujo, instrucciones adicionales, switcch, bulces y bifurcaciones

Estos flujos de trabajo se crean con un editor de texto como Azure portal o Visual Studio , ademas los flujos se conservan en un archivo [[ JSON]]



--------------

<h2> Diferencias
--------------

Ademas algunas diferencias de Azure Functions y Logic son las siguientes:

- Sabemos que Functions y Logic Apps pueden crear [[Orquestación]] complejas.

- Con Functions unicamente escibrimos código para completar cada paso

- Con  Logic Apps, se usa una [[GUI]] para definir las acciones y como se relacionan entre si

- Su enfoque es para automatizar un proceso de negocio

- Se caracteriza por contenedores prestablecidos y personalizados

-  Azure Functions es un servicio informático sin servidor, y Azure Logic Apps está diseñado para ser un servicio de orquestación sin servidor

-  Los precios de Azure Functions se basan en el número de ejecuciones y en el tiempo ejecución de cada una.

<h2> Función
--------------

Azure Logic Apps puede ejecutar una lógica que los servicios de Azure desencadenan sin escribir codigo, las aplicaciones se puede compilar vinculando desencadenadores.

_Un desencadenador es un evento (como un temporizador) que hace que una aplicación se ejecute, que un mensaje nuevo se envíe a una cola o que se emita una solicitud HTTP. Una acción es una tarea o paso que se puede ejecutar._

<h2>  Cuando Usarlo?
--------------

Util para:
- realizar una orquestación entre API conocidas

- tareas automatizadas escritas en un lenguaje de programación imperativo

Logic Apps es excelente a la hora de conectar una gran variedad de servicios distintos mediante sus API para pasar y procesar los datos a través de los muchos pasos de un flujo de trabajo.