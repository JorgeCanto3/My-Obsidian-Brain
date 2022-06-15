<h1>Azure Functions

----

<h3>Caracteristicas

Azure Functions es un servicio [[ServerLess]]

Modelos: PaaS - Serverless

---
<h3>Descripcion
-
Con este servicio nos encargamos unicamente ejecutar el  codigo de un servicio, ya que la infraestructura es encargada por aquel que nos brinda el servicio. Su funcion y cobro es  unicamente por el tamaño y evento ( Por cada vez que se nos es llamado). Una función de Azure es un entorno sin estado. Una función se comporta como si se reiniciara cada vez que responde a un evento. 

Puede hospedar un único método o función mediante un lenguaje de programación popular en la nube que se ejecuta en respuesta a un evento. como mensajeria de Iot o bien API's sencillas. 

---
Cuando son sin estado (valor predeterminado), se comportan como si se reiniciaran cada vez que responden a un evento. 

Cuando son con estado (denominado Durable Functions), se pasa un contexto a través de la función para realizar el seguimiento antes de la actividad.

---

Azure puede realizar tareas de orquestración con Durable Functions

Si cambian las necesidades de la aplicación del desarrollador, se puede implementar el proyecto en un entorno que no sea sin servidor. Esta flexibilidad permite administrar el escalado, ejecutar en redes virtuales e incluso aislar por completo las funciones.

Puede servir para diversos propositos en el diseño de apps, sus funciones se pueden escribir con C#, Python, JavaScript, Typescript, Java y PowerShell.

Las funciones son un componente clave de la informática sin servidor

Las funciones pueden ser sin estado o con estado.
---
<h3> Escalabilidad
-
La escalabilidad en Functions sera de manera automatica, esta dependera de la demanda que suele varia de desde dias con muchos eventos a dias con eventos nulos.

Azure Functions se puede escalar horizontalmente para adaptarse a esas horas de más trabajo.

----
<h3>Beneficios
-
Con el uso de Azure Functions reduciremos costos, ya que al unicamente pagar los eventos pedidos sera menos. En cambio con una maquina virtual con un costo incluso mayor, donde ademas esta maquina a pesar de estar inactiva seguira teniendo un costo

Es ideal si le preocupa solo el código que ejecuta el servicio y no la infraestructura o la plataforma subyacente.

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

<h2>  Cuando Usarlo?
--------------

Util para ejecutar algoritmos personalizados o realizar análisis y búsquedas de datos especiales

Azure Logic Apps puede ejecutar la lógica (bucles, decisiones, etc.), si tiene una orquestación de lógica intensiva que requiera un algoritmo complejo, la implementación de ese algoritmo podría ser más detallada y visualmente abrumadora.