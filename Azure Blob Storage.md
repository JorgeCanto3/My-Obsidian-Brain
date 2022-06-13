# Azure Blob Storage
## _Aspectos Basicos_
Azure Bolb Storage es un servico para el almacenamiento de objetos para la nube, capaz de almacenar grandes cantidades de datos como texto o binario. Este servicio no es estructurado por ende no hay restriccion sobre los tipos de datos que puede contener.

Puede Almacenar miles de cargas simultáneas , grande datos de video y es accesible desde alguna conexion con internet.

No se limita a formatos de archivo comunes, este podria contener gigabyetes de datos binarios o datos para el desarrollo de una App Web

**No requieren ser administrados ya que Azure se encarga del Almacenamiento Fisico**


**Los blobs se almacenan en contenedores, lo que ayuda a organizar los blobs en función a las necesidades**


_Ejemplo_ de cuentas con contenedores y blobs
![[Pasted image 20220608182503.png]]

<h3> Niveles de Acceso de Blobs

Azure proporciona niveles de acceso, que puede usar para equilibrar los costos de almacenamiento con sus necesidades de acceso. Los niveles dfe acceso disponibles son:

- **Nivel de acceso frecuente (Hot)** :
	-  Optimizado para almacenar datos a los que se accede con frecuencia

- **Nivel de acceso esporádico (Cold)** : 
	- Optimizado para datos a los que se accede con poca frecuencia y que se almacenan al menos durante 30 días

- **Nivel de acceso de archivo (Archive)** : 
	- Conveniente para datos a los que raramente se accede y que se almacenan durante al menos 180 días con requisitos de latencia flexibles

![[Pasted image 20220608190300.png]]


