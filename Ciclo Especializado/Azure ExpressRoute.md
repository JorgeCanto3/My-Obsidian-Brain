# Azure ExpressRoute


- ExpressRoute permite ampliar las redes locales a la nube de Microsoft mediante una conexión privada con la ayuda de un proveedor de conectividad. Podemos establecer conexiones con servicios en la nube de microsoft.

- La conectividad puede ser desde una red de conectividad universal, estas conexiones de ExpressRoute no pasan por la red publica, asi se ofrece más confiabilidad, más velocidad, latencia coherentes y mayor seguridad que las conexiones normales a través de Internet.

![[Pasted image 20220608005201.png]]

#### Ventajas
- Conectividad de nivel 3 entre su red local y Microsoft Cloud a través de un proveedor de conectividad.

-   Conectividad de servicios en la nube de Microsoft en todas las regiones dentro de la región geopolítica.

-   Conectividad global a los servicios de Microsoft en todas las regiones con el complemento ExpressRoute Premium.

-   Enrutamiento dinámico entre la red y Microsoft a través de BGP.

-   Redundancia integrada en todas las ubicaciones de configuración entre pares para una mayor confiabilidad.

-   El tiempo de actividad de conexión SLA.

#### Caracteristicas
<h5> Conectividad de nivel 3

- Proporciona conectividad de nivel 3 (nivel de dirección) entre la red local y la nube de Microsoft a través de asociados de conectividad.

<h5> Conectividad con los Servicios en la nube de Microsoft

- Permite acceso a los siguientes servicios a todas las regiones
	
	-   Microsoft Office 365
	-   Microsoft Dynamics 365
	-   Servicios de proceso de Azure, como Azure Virtual Machines
	-   Servicios en la nube de Azure, como Azure Cosmos DB y Azure Storage

<h5> Conectividad local con Global Reach

- Se puede permitir que Global Reach de ExpressRoute intercambie datos entre los sitios locales si conecta los diferentes circuitos ExpressRoute.

<h5> Enrutamiento dinámico

- Este protocolo permite el enrutamiento dinámico entre la red local y los servicios que se ejecutan en la nube de Microsoft.

<h5>  Modelos de conectividad de ExpressRoute

- Se admiten los iguietne modelos para conectrar la red local con la nube:

	-   Ubicación de CloudExchange
	-   Conexión Ethernet de punto a punto
	-   Conexión universal
	-   Directamente desde sitios de ExpressRoute

<h3> Seguridad

- Con ExpressRoute los datos no viajan a través de la red pública de Internet y, por tanto, no se exponen a los posibles riesgos asociados a las comunicaciones de Internet. ExpressRoute es una conexión privada de la infraestructura local a la infraestructura de Azure.

Cuenta con conetividad privada pero no está cifrada 