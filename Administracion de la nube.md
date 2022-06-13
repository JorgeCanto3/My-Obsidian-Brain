# Administracion de la nube

<h3>Azure Portal

<h6><center>Portal.azure.com

- Portal web para navegadores donde podemos, usar, controlar, administrar , borrar, crear, escalar, gestionar recursos. Tenemos acceso a los servicios de Azure de la nube

<h3>Azure App

- Nos permite realizar cosas mas sencillas desde la app como apagar, borrar o reiniciar recursos ademas podemos ver:
	- Grupos de recursos
	- Recursos
		- Las propiedades
	- Nuestras Suscripciones
		- Gestionarlas 

- No podemos crear recursos desde la App pero con el Cloud Shell Integrado si podemos crear servicios.


<h3>Azure CLI (Comand Line Interface)

		No es compatible con Chromebook

- Este servicio nos permite manejar e instalar  nuestro entorno de azure con comandos. Este es compatible con **Windows, Linux, Mac y Azure Cloud Shell**


<h3>Azure Cloud Shell 

- Este servicio es en la nube y funciona en cualquier navegador de la nube, para poder velocidada, accesp por ssh, uso con git,etc

<h3>PowerShell

- Linea de comandos de microsoft
	- <h6> Azure PowerShell

		- Sirve para automatizar tareas por linea de comando, disponible en Windows, Mac y Linux pero no en ChromeBook. Administramos azure de manera remota

<h2>Recursos de Azure SaaS

	 Los nombres de los servicios de azure son implicitos y nos dan una idea sobre lo que puede tratar

<h3> Azure Service Health

- Con este servicio podemos revisar el estado de nuestros recursos, podemos ver si el servicio de azure esta fallando
 
	- Podemos crear una alerta para cuando cierto servicio falle, para **Cualquier region del mundo**

<h3> Azure Monitor

- Monitorea el rendimiento de nuestras recursos, si se esta usando mucho Procesador, Ancho de Banda, CPU, Memoria. Podemos crear alerta ded rendimineto ademas de ver posibles errores de implementacion


<h3> Azure Advisor    

	Usa IA

- Advisor no asesora o recomienda sobre las configuraciones para aumentar la seguridad, el rendimiento o bajar los costos. Nos puede ayuda al cumplimiento y eficiencia de la nube


<h3> Plantillas ARM (Azure Resource Mangement)

- Las plantillas nos sirven para ahorranos trabajo y ejecutarlos varias veces en distinitos proyectos

<h3> DevOps (Developer Operations)

- Ayuda al equipo de desarrollo de software a automatizar y hace eficaces nuestros procesos. Aborda cada fase de ciclo de vida del desarrollo de software, meora la gesion de software y se puede implementar con App service o Functions
	
	- Cuenta con:
		
		- **Azure Repos**:
			- Repo de github


		- **Azure Boards**:
			- Ayuda al gestionamineto del proyecto

		- **Azure Pipelines**:
			- Herramiento de automatizacion de canalizacion de:
				-  CI: Continuos Integration
				
					- Integracion continua, para cuando agreguemos algun cambio reciba un testing y se ejecute a la nueva version
					
				- CD: Continuos Deplpyment
					- Cuando subimos un cambio es directo
					
		- **Azure Artifacts**:
			
			- Repo para poder  guardar los codigos ya compilados, listo para ejecutar y estan seguras en ese repo 
		 
		- **Azure Artifacts**:
		
			- Herramienta de automatizacion de test que pueden ser usadas por una canalizacion de CI y CD
			
		-  **Azure DevTest Labs**
			-  Automatiza la configuración y anulacion de máquinas virttuales. Sirve para automatizar prubas
			
				- Automatiza la creacion y gestion de las  maquinas virtuales para probar codigo
					- Puede crear, eliminar, agregar
				
				- Cualquier cosa que se pueda implementar con una ARM se puede implementar se puede implementar con DevLabs 