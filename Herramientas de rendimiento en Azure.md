# Herramientas de rendimiento en Azure
Azure nos proporciona distintas herramientas con las cuales podemos cuidar el rendimiento de nuestro servicio u aplicaion, podemos combinar distntas soluciones y poder: 

-   Obtener respuestas, información y alertas para asegurarse de que ha optimizado el uso de la nube.
-   Determinar la causa principal de los problemas no planeados.
-   Prepararse de antemano para interrupciones planeadas.

Las opciones de Azure son varias pero las tres principales para cuidar o manejar el rendimiento son:

- Azure Advisor: 

	- Adivsor evaluo los recursos y nos hace recomendaciones para mejorar la seguridad y rendimiento para una exelencia operativa y poder reducir los costos. Estas hecho para reducir costos, tiempo y opitimizar la nube. Las recomendaciones estan disponibles en [Portal](portal.azure.com)  y la API ademas podemos aplicar al momento, posponerlas o descartarlas 
	
	- Las recomendaciones se dividen en cinco categorias que son: 

		- Confiabilidad
		- Seguridad
		- Rendimiento
		- Costos
		- Excelencia Operativa

- Azure Monitor:

	- Monitor permite recopilar, analizar y mostar datos asi como realizar funciones de las métricas y los datos registradosen todo el entorno local y de Azure. **_Ejemplo_**
		
	![[Pasted image 20220614190707.png]]
	- _Descripcion del esquema_

		- Del lado izquierdo vemos los origenes de los datos de las metricas y los registros. Estos se puede recopilar desde el S.O hasta la red
	
		- En el centro el almacenamiento de los datos,  su registro y  metricas
	 
		- Del lado derecho se encuentra las formas en que podemos utilizar los datos. Podemos ver su rendimiento historico o en tiempo real o ver informacion detallada
		
	-  Con monitor podemos responder ante eventos criticos con alertas enviadas por SMS, correo electronico. Asi mismo podemos usar un desencadenador por si hay alta o poca demanda se realice un escalado automatico


- Azure Services Health

	- Nos da una vista personalizada de los servicios, regiones y recursos de azure, que nos muestra los problemas detectados que afecta de manera generalizada a los clientes de Azure.

	- Muestra los problemas detectectados de mayor a menor importancia los servicios que le afectan

	- Los problemas son poco frecuentes pero es ideal prevenir con alerta para evaluar las interrupciones, despues de una interrupcion se nos proporcionan informes con las causas

	 - A su vez podemos supervisar varios tipos de eventos como:
	 
		 - Problemas de servicio:
			 - Como interrupciones que afecten al momento
			 
			 - Podemos profundizar en los servicios y las regiones afectados
	
		-  Mantenimiento planeado: 
			- Podemos ver los servicios y regiones para ver la afectacion como  influirá un evento y qué debe hacer.
			
			- Si el servicio requiere un reinicio podemos seleccionar cuando queremos este 

		- Avisos de estado
			- Problemas a los cuales debemos actuar para evitar la interrupcion de nuestro serivicio. Se avisan con antelación

<h2> Criterio de Decision

<h6>Para Azure Advisor

Cuando necesitamo analizar cómo usamos Azure para reducir los costos, mejorar la resistencia o reforzar la seguridad es recomendable usar Azure Advisor, ya que Adivsor analiza la configuracion, uso de los recursos  y nos da sugerencias para optimizar y reducir costos

<h6>Para Azure Service Health

Si necesitamos supervisar los servicios de Azure es ideal Service Health para mantener el control de Azure. asi podemos ver las proximas interrupciones y hacer un plan ante esto, asi como los servicios que se lanzarán.

<h6>Para Azure Monitor

Para un rendimiento o problemas con la maquina virtual, instancias, contendores es idoneo utilizar Azure Monitor y crear informes y notificaciones para entender el rendimiento de nuestros servicios o diagnosticar problemas. Tambien podemos medir eventos personalizados (** como agregados al codigo fuente de la aplicaciones de software** )y datos de telemetria y por ultimo  podemos configurar alerta de eventos relacionados con recursos especificos