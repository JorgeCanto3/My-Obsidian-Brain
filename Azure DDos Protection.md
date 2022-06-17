# Azure DDos Protection
Azure DDos Protection sirve para proteger los recursos de ataques DDos pero tenemos que empezar con que son los ataques DDos.

----
## ¿Que son los ataques DDos?

Los ataque DDos o bien ataques de denegacion de servicio distribuido, intenta sobrecargar y agotar los recursos de una aplicación, provocando que la misma se vuelva lenta y no responda bien a los usuarios. Estos ataques pueden estar enfocados a cualquire recurso al cual sea posible acceder mediante el internet publico, inlcuidos sitios web.

--------

Ahora que ya conocemos los ataques DDos tenemos que conocer como es que funciona Azure DDos

----
## ¿Que es Azure DDos protection?
Como sabemos Azure DDos Protection nos protege ante los ataque DDos,  no ayuda a proteger las aplicaciones de Azure analizando y descartando el trafico de DDos en la red de azure antes de que afecte la disponibilidad. Ademas si combinamos la seguridad recomendada en nuestros servicos, esto es una defensa adicional ante los ataques.

Cuando se ataca DDos Protection usa la escala y la elasticidad de lar ed global de microsoft para incorporar la capacidad de mitagiacion de DDos en cada region.

_Ejemplo de un ataque y como llega a los clientes_

![[Pasted image 20220617162133.png]]

Protection identifica el intento de sobrecargar la red y evita que estes trafico llegue y se asegura que no llegue a los servicios, mientras que el trafico legitimo de los clientes no s interrumpido.

Tambien este serivicio nospuede ayudar a administrar el consumo de la nube, con la version Estandar nos ayuda a garantizar que la informacion que se procesa refleje el uso del cliente. 

_Podemos recibir creditos por costos acumulado por un ataque DDos, cuando se escale horizontalmente los recusos _

### Niveles de servicio de DDoS

- **Basico**
	- Este nivel se habilita de forma automática sin costo como parte de la suscripcion de Azure
		- En el se supervisa de manera continua el trafico y la mitigación en tiempo real  de ataques de nivel red comunes. 
		- Garantiza que la infraestructura  de Azure no se vea afectada durante un ataque DDoS a gran escala

- **Estandar**
	- Ofrece funcionalidades adicionales para la mitación adaptadas especificamente para los recursos de [[Azure Virtual Network]]. No se requiere ningun cambio en la aplicación
		- Al igual que el basico supervisa el trafico de manera continua y mitiga ataques comunes de red.
		- Las directivas o reglas  de protección se ajustan a través de la supervisión del tráfico dedicado y los algoritmos de [[Azure Machine Learning]], estas directivas se aplican a direcciones IP públicas asociadas a recursos implementados en redes virtuales, como Load Balance o App Gateway 

 _Con la red global se puede distribuir y mitigar el tráfico de ataque entre regiones de azure_

### Ataques que evita 

En el nivel estandar puede evitar:

- **Ataques volumétricos**
	- Desborda la capa de red con una gran cantidad de tráfico que parece legítimo

- **Ataques de protocolo**
	- Convierten un destino inaccesible al aprovechar una vulnerabilidad en el protocolo 

- **Ataques de nivel de recursos (Nivel de aplicación**)(**Solo con el firewall de apps web**)
	- Se centran en los paqutes de las apps web par interrumpir la transmisión de datos entre hosts. Para protegerse se necesita un firewall de app web (WAF)


_DDoS Protection Estándar protege el firewall de aplicaciones web de los ataques de protocolo y volumétricos._