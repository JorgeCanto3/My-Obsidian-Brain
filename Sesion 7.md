# Sesion 7
## Administración en la nube
###  [Azure Portal](https://portal.azure.com/)

Es un portal web para navegadores donde podemos usar todo lo de la nube. Administrar los recursos, crear, elminar recursos, administar permisos, escalar. Podemos hacer TODOOOO

### [[App de Azure]]
Disponible para android y IO's

Nos permite administar situaciones pequeñas de la nube y no tenemos un acceso totaaaal como con [Azure Portal](https://portal.azure.com/). Podemos apagar recursos, reiniciar recursos, podemos ver nuestros grupos de recusos

Pero podemos utilizar el [[Azure Cloud Shell]] Integrado para hacer acciones un poco más elaboradas como crear recursos

Con el Azure CLI posdemos crear recursos

### Azure CLI (Comand Line Interface)

Es una forma de manejar con comandos nuestros servicios de azure. No es compatible con el Chromebook, solo Windows, Linux y Mac.

Podemos crear grupos de recursos, recursos, etc

**Practica min 27:48**

### [[Azure Cloud Shell]]

Azure cloud shell es un CLI en la nube. Terminal de comando en la nuce para velocidad, acceso por ssh, git, etc.

### Azure PowerShell

 Powershell es una linea de comandos de microsoft util en windows pero tambien existe el Azure PowerShell es para manejar la nube de Azure, su funcionalidad es igual a las demas pero depende del conoscimiento de las personas en cuanto a Sistemas operativos Usamos PowerShell si estamos familiarizados con Windows y Bash si lo estamos con Linux.

Ventana Azul, Solo disponible en Windows, Mac y Linux. Pero tampoco esta disponible en ChromeBook

------------------------------
### [[Azure Service Health]]
**SaaS**

Sirve par checar la salud de nuestros serivicos, nos avisa de manetiminetos programados. Podemos ver si un servicio de Azure esta fallando en una region o a nivel global.

Tenemos que recurir a este servicio cuando algo esta fallando

**Sin cobro y Sin SLA**

**Practica min 40**

### Azure Monitor
**SaaS**
**Sin cobro y Sin SLA**

Monitorea el rendimineto de nuestras aplicaciones, nos da aletras del rendimineto unicamente de nuestras aplicaciones, nos dice si estamos usando mucho ancho de banda, CPU, Memoria. 

Tambien podemos ver posibles fallas al implementar algun recursos y crear alertas sobre lo que sucede con nuestros recursos y las recibiremos a nuestro correo

**Cobro por alertas de metrica**

**Practica min 55**

### Azure Advisor
**SaaS**

Advisor nos recomienda sobre las cosas que podemos mejorar en nuestros recursos, para poder gastar menos, mejorar nuestra seguridad. Tambein podemos crear alerta 

### Plantillas ARM (Azure Resource Mangement)
Sirve para poder replicar los grupos de recursos, en estas plantillas se contiene todo lo que hizo azure para generar esa plantilla y la podemos utilizar para crear otro.

Tambien sirve para documentar nuestro Grupo de recursos

practica 1:22:00

## DevOps (DeveloperOperations)
Ayuda a los equipos de desarrollo de software a automatizar y hacer eficientes sus procesos.

Automatizamos el proceso de programaicion, IA, Ciencia ded datos, Arquitectura de soluciones, Tests, etc.

Se hace más eficentos los procesos de los prgramadores

### Azure DevOps
**SaaS**

Aqui se guarda codigo en repositorios como Github pero aqui es un entorno empresarial y mas privado

Es un servicio que aborda cada fase del ciclo de vida del desarrollo de software, mejorando la gestion de software y hacemos más productivo el codigo de una empresa

Este se puede implementar con App Service o Azure Functions

Los serivicios de DevOps son los siguientes

#### Azure Repos
Repositorios de codigo centralizado en las empresas

#### Azure Boards
Gestionamos el proyecto con más facilidad con paneles Kanabn 

#### Azure Pipelines
Automatizamos los canales de CI (Continuos Integrecion, incluye pruebas antes de ser integrado )y CD (Continuos Deployment, se sube al momento)

#### Azure Artifacts
Hospeadamos codigos fuentes compilados y los alamacena de forma segura. Es un repo pero con el codigo compilado

#### Azure Test Plans
Pruebas automatizadas que podemos utilizar en la canalizacion de CI/CD

### Github 
Es casi lo mismo a Azure DevOps pero la diferencia es que DevOps es para un entorno empresarial y Github es un open source con el fin de colaborar con distintas personas

Cuenta con muchos sevicios como CodeSpaces, Actions entre otros servicios.
Los codespaces son un entorno en la nube para ejecutar un codigo y es posible programar en cualquier lado :D

**Practica**
### Azure DevTests Lab

Automatiza la creacion y gestion de pruebas o maquinas virtuales para probar codigo, podemos implementar cualquier cosa que se haga con una plantilla ARM

En otras palabras crea una MV para realizar pruebas de codigo