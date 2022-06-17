# Azure Firewall
<h6>Introducción al servicio

<h5> <center> ¿Que es un Firewall ?

Un firewall es un dispositvo de seguridad de red que supervisa el trafico entrante y saliente, este decide si se permite o bloquea un traffico en función de un conjunto definido de reglas de seguridad.

Se pueden crear reglas de firewall que especifiquen intervalos de direcciones IP. Solo a los clientes que se les otorgaron IP's en los intervalos pueden tener acceso. Estas reglas tambien pueden incluir información especifica de puertos y protocolos de red 

<h5> <center> ¿Que es Azure Firewall?

Azure Firewall es un servicio de seguridad de red administrado, basaddo en la nube que ayuda a proteger los recursos **en las redes virtuales de Azure**.

Las redes virtuales son similares a una red tradicional con la cuales trabajariamos en nuestro propio centro de datos, las redes virtuales requieren de este servicio para poder comunicarse de forma segura entre sí, con internet y con redes local. 

_Azure Firewall representado con un diagrama_

![[Pasted image 20220616190718.png]]

Azure Firewall es un firewall con estado, un firewall conestado analiza el contexto completo de una conexión de red, no de manera checa de manera individual la red. 

Incluye alta disponibilidad y escalabilidad en la nube sin restricciones.

Azure Firewall proporciona una ubicación  central para crear, aplicar y registrar directivas de conectividad de red y aplicaciones entre sucripciones y redes virtuales. Se utiliza una IP pública estática para los recursos de redes virtuales , esto permite que los firewall externo identifiquen el tráfico entrante de redes virtuales.

Azure Firewall cuenta con distintas caracteristicas, como:

-   Alta disponibilidad integrada
-   Escalabilidad en la nube sin restricciones.
-   Reglas de filtrado entrante y saliente.
-   Compatibilidad con la traducción de direcciones de red de destino (DNAT).
-   El registro de Azure Monitor.

Se suele implementar para controlar el acceso general a la red.

Podemos configurar:

- Reglas de aplicación
	- Definen los nombres de dominio completos (FQDN), a estos solo se puede acceder desde una subred

- Reglas de red
	- Definen la dirección de origen, el protocolo, el puerto de destino y la dirrección del destino 

- Reglas de traducción de direcciones de red (NAT)
	- Definen los puertos y las direcciones IP de destino para traducir las solicitudes entrantes


_[[Azure Application Gateway]] tambien cuenta con un firewall, llamado firewall de aplicaciones web(WAF), proporciona protección entrante centralizada para las aplicaciones web contra vulnerabilidades de seguridad comunes._


**Azure Frotn Door y [[Azure CDN (Content Delivery Network)]] tambien proporcionan firewall para apps web**

