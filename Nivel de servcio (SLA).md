# Nivel de servcio (SLA)
un _Acuerdo de Nivel de Servicio_ (SLA) es un contrato formal entre una empresa de servicios y el cliente.

El tiempo de actividad garantizado para los servicios de Azure de pago en el SLA es, como mínimo 99,9%

## Importancia

La comprensión del acuerdo de nivel de servicio de los servicios de Azure que use le ayudará a conocer las garantías que puede esperar.

Comprender los acuerdos de nivel de servicio implicados puede ayudarle a definir el acuerdo de nivel de servicio que establezca con los clientes.

### Conocer el SLA de Azure

Puede acceder a los acuerdos de nivel de servicio desde [Contratos de nivel de servicio](https://azure.microsoft.com/support/legal/sla/).

Cada serivicio de Azure cuenta con su propio SLA

### SLA tipico

-   **Introducción**
    
    En esta sección se explica qué esperar del acuerdo de nivel de servicio, por ejemplo, su ámbito y la repercusión que las renovaciones de suscripción pueden tener en las condiciones del acuerdo.
    
-   **Términos generales**
    
    Esta sección contiene los términos empleados en todo el acuerdo de nivel de servicio, de modo que ambas partes (el cliente y Microsoft) entiendan y compartan el mismo vocabulario. Por ejemplo, en esta sección se puede definir el significado de tiempo de inactividad, incidentes y códigos de error.
    
    En esta sección también se definen las condiciones generales del acuerdo, que incluyen una explicación de cómo enviar una demanda o recibir créditos por cualquier problema de rendimiento o disponibilidad, así como las limitaciones del acuerdo.
    
-   **Detalles del Acuerdo de Nivel de Servicio**
    
    En esta sección se definen las garantías específicas del servicio. Los compromisos de rendimiento se miden normalmente en porcentajes, que normalmente están comprendidos entre el 99,9 % ("tres nueves") y el 99,99 % ("cuatro nueves").
    
    Por lo general, el compromiso de rendimiento principal se centra en el _tiempo de actividad_, es decir, en el porcentaje de tiempo que un producto o servicio está operativo y sin problemas. Algunos acuerdos de nivel de servicio se centran también en otros factores, como la _latencia_ o la rapidez con la que el servicio debe responder a una solicitud.


## Tiempo de inactividad

El _tiempo de inactividad_ es el período de tiempo que el servicio no está disponible.

### Porcentajes en el tiempo de inactividad

La diferencia entre el 99,9 % y el 99,99 % puede parecer pequeña, pero es importante comprender lo que significan estos números en cuanto al tiempo de inactividad total.

![[Porcentajes.jpg]]


_El tiempo es acumulativo_


## Creditos de Servicio
Un _crédito de servicio_ es el porcentaje del precio que ha pagado que se le abonará conforme al proceso de aprobación de reclamaciones.

![[Creditos.jpg]]


##### Los servicios gratiutos no tienen SLA

###  Conocer la interrupcion de un servicio

[Estado de Azure](https://status.azure.com/status) proporciona una visión global del estado de los servicios y las regiones de Azure.

Desde la página estado de Azure también puede acceder a Azure Service Health, que proporciona una vista personalizada del estado de los servicios y las regiones de Azure que está usando, directamente desde Azure Portal.

### Solicitar un crédito de servicio a Microsoft

Presentar un  reclamación a Microsoft para recibir un crédito de servicio. Si adquirimos los servicio por medio de un partner este se encargara

Cada acuerdo de nivel de servicio especifica el plazo en el que se debe enviar la reclamación y el plazo para que Microsoft la procese.


### Acuerdo de nivel de servicio de la aplicación

Define los requisitos del acuerdo para una aplicación específica

### Patrones de uso

Los _patrones de uso_ definen cuándo y cómo acceden los usuarios a la aplicación.

###  Cargas de trabajo
Una _carga de trabajo_ es una función o tarea distinta que se separa lógicamente de otras tareas, en términos de requisitos de almacenamiento de datos y lógica empresarial. Cada carga de trabajo define un conjunto de requisitos para la disponibilidad, la escalabilidad, la coherencia de los datos y la recuperación ante desastres.

### Combinación de los acuerdos de nivel de servicio para calcular un SLA compuesto

El proceso de combinación de acuerdos de nivel de servicio ayuda a calcular el _acuerdo de nivel de servicio compuesto_ para un conjunto de servicios. Para calcular el acuerdo de nivel de servicio compuesto, hay que multiplicar el acuerdo de cada uno de los servicios.

![[cOMPUETSOP.jpg]]
Recuerde que necesita dos máquinas virtuales. Por lo tanto, el acuerdo de nivel de servicio de Virtual Machines del 99,9 % se incluye dos veces en la fórmula.


## Ciclo de vida de un servicio

Es la forma en que cada servicio de Azure se pone a disposición del público

Cada servicio de Azure empieza con fase de desarrollo. En esta fase, el equipo de Azure recopila y define los requisitos y comienza a crear el servicio.


## Aumentar el tiempo de actividad

