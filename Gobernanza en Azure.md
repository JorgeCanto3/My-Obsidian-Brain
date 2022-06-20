
# Gobernanza en Azure

## Gobernanza 

Es el proceso en el cual se establecen reglas y directivas y se garantiza que estas se aplican. 

Al tener uana buena estrategia de gobernanza ayuda a tener un control de aplicaciones y los recursos que se administran en la nube. 

Con el control no aseguiramos de que sea compatible con:

- Estándares del sector como PCI DSS
- Estándares corporativos o de la organización
	- Como asegurarse que los datos de la red esten cifrados

Las ventjas de gobernanza son mayore cuando:

- Hay varios equipos de ingeniería 
- Varias suscripciones que administar
- Requisitos normativos que deben aplicarse
- Estándares que seguir en todos los recursos de la nube

## Control de acceso basado en roles (RBAC de Azure)

Azure proporciona roles integrado que describen las reglas de acceso comunes de los recurso en la nube. Asi mismo tambien podemos definir nuestros propios roles

Cada rol tiene un conjunto asociado de permisos de acceso. Cuando asinamos los roles a los usuarios o grupos reciben los permisos de acceso asociados correspondientes

El RBAC se apllica a un ámbito, que es un recurso o un conjunto de recursos en los que este acceso se permite

_Diagramas de roles y ambitos_

![[Pasted image 20220618113014.png]]

Los ámbitos pueden ser:

- Un grupo de administración (Colección de varias suscripción)
- Una sola suscripción
- Un grupo de recursos
- Un solo Recurso

**Aplicarlo**

RBAC de azure se aplica a cualquier acción que se inicie en un recurso de Azure que pasa por Azure Resource Manager. Recordemos que manager es un servicio de administracion que proporciona una forma de protegey organizar nuestros recursos

Se accede a este servicio por medio de Portal, Cloud Shell. PowerShell o la CLI

RBCA como sabesmo emplea un modelo de permisos, al asginfarnos un rol nos permite realizar determinadas acciones como podria ser leer, escribir o eliminar

**A quien se aplica**

Se puede aplicar a una persona individual o a un gupo pero tambien a otros tipode de entidades especiales como servicio e identidades administradas.

Las aplicaciones y servicios usan estos tipos de identidad para automatizar el accesos.


**Administrar  permiso de RBAC**

Se administrar en el panle de Control de Acceso (IAM) de Azure Portal. Ahí se muesta quien tiene acceso a qué ámbito y los roles que se aplican, en el mismo podemos conceder o quitar cualquier tipo de acceso.

![[Pasted image 20220618124442.png]]


## Bloqueo de Recursos 

El bloqueo impide que se eliminen o modifiquen recursos por error, es un sistema de aviso que nos recierda que un recurso no se debe elminar o cambiar

Los bloqueaos se pueden administrar en  Azure Portal, PowerShell, la CLI de Azure o una plantilla ARM

![[Pasted image 20220618124938.png]]

#### Niveles de bloqueo

- **CanNotDelete**
	- Con esto los usuarios autorizados pueden seguir leyendo y modificando un recurso pero no eliminar sin quitar el bloqueo

- **ReadOnly**
	-  Los usuarios autorizados solo pueden leer el recurso, no pueden hacer cambios ni eliminar


**Modficar o quitar bloqueo**

Podemos modifcar un recurso quitando, quitando el bloqueo. despues de quitarlo podemos realizar cualquiera accion a las cuales tengamos permiso

Estos bloqueo son independientes de RBAC

### Combinacion de bloqueo con Azure BluePrints

Si combinamos los bloqueos de recursos con los blueprints se crea una protección más rigurosa. Con Blueprints nos permite defiinir el conjunto de recursos estandar que Azure necesita

Con los Blueprints podemos crear un plano técnico que especifique que debe haber un bloqueo de recurso determinado ademas podemos remplazar el bloqueo de recursos si el bloqueo se quita

## Etiquetas para los recursos

Las etiquetas son una forma de poder organiuzar lor recursos, proporcionando información extra, o metadatos, sobre los recursos. Estos metadatos son útiles para lo siguiente:

- **Administración de recursos**:
	- Las etiquetas permiten encontrar recursos asociados con cargas de trabajos y poder actuar

- **Optimización y administración de costes**
	- Pemirten agrupar recursos par informar sobre los costes, manteniendo el presupuesto a raya y predecir costes estimado

- **Administaracion de operciones**
	- Agrupan los recursos segun su importancia

- **Seguridad**
	- Permite calsifica los datos segun su nivel de seguridad como los publicos o confidenciales

- **Gobernanza y cumplimiento normativo**
	- Podemo identificar los recursos que cimplen para de gobernanza y cumplimiento normativo

- **Automatización y optimización de las cargas de trabajo**
	- Podemos organizar los recursos que participan en implementaciones complejas 


**Modificacion de etiquetas**

Podemos moficar las etiquetas por distintos medios como PowerShell, la CLI de Azure, plantillas de Azure Resource Manager, la API REST o Azure Portal.

*Estas etiquetas pueden ser administradas port Azure Policy*. Con policy podemos garantizar que un recurse herede las mismas etiquetas que su grupo de recursos primarios, tambien es usado para crear nuevas reglas y conveciones de etiquetado

Una etiqueta se compone de lo siguiente

- **Nombre**

	- **Valor**

- **AppName**

	- Nombre de la aplicación de la que forma parte el recurso

- **CostCenter**

	- Código interno del centro de costes

- **Propietario**

	- Nombre del propietario de empresa responsable del recurso

- **Entorno**

	- Nombre de entorno, como "Prod.", "Dev." o "Prueba".

- **Impacto**

	- Importancia del recurso para las operaciones empresariales, como "Crítico", "Gran impacto" o "Bajo impacto".

![[Pasted image 20220618173007.png]]

Para poder controlar y auditar recursos podemos utilizar

- [[Azure Policy]]

Para poder hacer gobernanza en Azure debemos usar

- [[Azure BluePrints]]


Aceleración del uso de la nube con [[Cloud Adoption Framework para Azure]]

## Gobernanza de suscripciones
Para la gobernanza en suscripciones  tenemos que tomar en cuenta 3 cosas

- Facturación
	- Se puede crear un informe de facturación por suscripción. Util para organizar las suscripciones de caa depto o por proyecto
- Control de acceso
		- Cada suscripcion esta asociada a un inquilino de Azure Active Directory , con esto los administradores pueden controlar la configurar un acceso granular a traves de  roles en el medio del control de acceso basado en roles
- Límites de suscripción
	- Las suscripciones también tienen algunas limitaciones de recursos.  Estos límites se deben tener en cuenta durante la fase de diseño. Si necesitamos superar estos límites, puede que tengamos que agregar más suscripciones. Si alcanzamos un límite máximo estricto, no hay flexibilidad para aumentarlo.

# Resumen

-   El control de acceso basado en roles de Azure (RBAC de Azure) permite crear roles que definen permisos de acceso.
-   Los bloqueos de recursos impiden que se eliminen o modifiquen recursos por error.
-   Las etiquetas de recursos proporcionan información extra, o metadatos, sobre los recursos.
-   Azure Policy es un servicio de Azure que permite crear, asignar y administrar directivas que controlan o auditan los recursos.
-   Azure Blueprints permite definir un conjunto repetible de herramientas de gobernanza y recursos de Azure estándar que la organización necesita.