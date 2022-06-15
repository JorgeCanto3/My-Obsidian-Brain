
# Herramientas de administracion en Azure 
Empecemos con:

### Herramientas de administracion

Existen dos categoria de Herramientas de administracio: Herramientas Visuales y Herramientas basadas en codigo


<h3> Herramientas Visuales

 Estas herramietnas nos proporcionan acesso completo y visualemente sencillo para poder trabajar azure en su totalidad de manera sencilla.

 Sin emabargo su desventaja recae al momento de requerir una gran implementacion de recursos.

<h3> Herramientas basadas en Codigo

Es una opcion Ideal al mometno de instalar, confugurar recursos, debido que al tener los codigos necesarios podemos guardar y repetirlos en el momento que se requiera, pero tenemos que mantenerlos actualizados para que el codigo siga siendo util.

 Este enfoque para administrar los recursos de hardware y en la nube, que usan los desarrolladores para escribir código de aplicaciones, se conoce como _infraestructura como código_.

------

<h3>  Infraestructura como código

La infraestructura como código tiene dos enfoques: Codigo Imperativo o Declarativo 

- **Codigo Imperativo**:

	- En este código se detalla cada uno de los pasos para lograr el resultado deseado

- **Codigo Declarativo**:

	- En este codigo solo se detalla el resultado y el lector o interprete es quien decide que camino o solucion debe tomar para alcanzar este resultado
	  
	-  Las herramientas basadas en código declarativo pueden proporcionar un enfoque más sólido para implementar decenas o cientos de recursos de forma simultánea y fiable.
---

<h2>Herramientas de Administracion de Azure

<h3>Azure Portal

El portal de azure es un interfaz de usuario basada en la web con esta podemos acceder a casi todas las caracteriticas y servicios de Azure.

 En este portal podemos encontrar una UI grafica con la cual podemos ecnotrar los servicios que estamos utlizando asi como crear nuevos, configurar los que tenemos y ver informe   

<h3>Azure Mobile App

 Azure Mobile App le permite acceder a los recursos de Azure desde iOS y Android, cuando no tiene el equipo a mano con esta app podemos:

- Supervisar el mantenimiento y estado de los recursos

- Consultar alertas, diagnosticos, resolver problemas rapidamente y reiniciar una app web o una MV 

- Ejecutar comadas del CLI o del Powershell para administrar los recursos

<h3>Azure PowerShell

Es un shell que permite ejecutar comandos denominados cmdlets o command-lets. Estros se les conoce como API REST de azure para realizar la administracion de todas las tareas posibles dentro de azure

Los cmdlets pueden ser ejecutados de dos formas, independientes o en combinarlos en un archivo en conjunto con estos podemos:

- Configurar rutina, anulacion y mantenimiento de uno o varios recurso

- Implementacion de una infraestructura completea que pueda conectar una gran cantidad de recursos
  
 Este proceso de comando se puesde repetir y automatizar en diversos S.O como Windows, Linux y Mac que es donde se encuentra disponible powershell o en su defecto podemos acceder a el mediante el Azure Cloud Shell en el navegador

<h2> CLI de azure

 CLI (Interefaz de linea de comando) de azure es un programa que permite ejecutar comando en Bash. Los API REST son lo comandos con los cuales podremos ejecutarlo para poder administar

 Al igual que en powershell pueden  ser indiviudales o en conjutno y podemos hacer las mismas acciones

 Es muy similar a Powershell en tanto en que S.O's funciona y como acceder la diferencia principal es la sintaxis. Tons elige la que te guste y ya


<h2> Plantillas de ARM

Las plantillas son una forma más sencilla y rapida de poder implementar las funcionalidades.

Las plantillas de Azure resource manager puede describirlos recursos que necesitamos en foramto JSON declarativo. Las plantillas se comprueban antes de ejecutar condigo para que los recursos de conecten y creen de manera correcta. Asi la plantila organiza la creacion de los recursos en paralelo (Al mismo tiempo).

Al crear una plantilla solo tenemos que denifir el estado y configuracion de cada recurso y ARM hace el resto.

Las plantillas pueden incluso ejecutar scripts de PowerShell y Bash antes o después de configurar el recurso.

<h2>Comparacion 

Con Azure PowerShell y la CLI de Azure permite obtener la IP de una MV implementada, reinicirala o escalarla. El Script realizado puede ser almacenado par relalizar este proceso de manera [[reiterada]]. Es ideal para tareas repetitivas o bien para encontrar rápidamente la configuración y la información con la que quiere trabajar.

Con ARM se define los requisitos y infraestructura de la app para implemnetarlo en distitntas ocasiones. Podemos utilizarlas de forma ocasional pero es mas util en cuestiones repetitivas sin embargo si es de un solo uso es mas sencillo los comandos o terminales.

Podemos utilizar scripts de Azure PowerShell y CLI en el ARM  para ppodert realizar tareas que no son posibles solo con la platilla, al combinar las herramientas tenemos la flexibilidad de elegir las ideonas para nostros

Con portal podemos adminsitrar casi todos nuestros servicios es buena opcion cuando solo tenemos que configurar y administrar recursos con poca frecuencia y preferimos una interfaz visual 

Por utilmo Azure Mobile App dado que tiene una cierta limitacion es mejor cuando no se cuente con un equipo y tenga que administar o evaluar problemas en el momento

Al usar PowerShell o CLI depende el entorno administrativo que vengamos, para Windoes es Power y Linux CLI

