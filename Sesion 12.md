# Sesion 12
## Gobernanza
En la gobernanza tenemos que hacer reglas y cumplir las mismas

### [[ Gobernanza en Azure]]
#### Directiva 
La directiva de azuer nos da un panorama sobre lo que esta pasando en le grupo de recursos. Podemos ver si una directiva eso no compatible con nuestro grupo de recusos o suscripcion

#### [[Azure Policy]] - Directory

Para empezar a usar azure como empresa lo ideal es crear nuestras reglas para poder manejar nuestros usuarios o colaboradoes, para despues trabar

Para poder crear reglas en nuestra nube, podemos hacerlo con Azure Directory siempre y cuando tengamos los permisos. Tambien podemos ver las reglas que no se han cumplido  

Directiva = Regla

Podemos asignar la regla para una grupo de recursos o para toda una suscripcion

Una  Inciativa es conjunto de directivas

Azure Blueprints (Plano tecnico) son un conjunto de iniciativas, funcionan para poder controlar mejor la nube y los usuarios 

Artefactos o Directivas son las directivas que asignamos dentro del plano tecnico. 

Podemos crear directivas con las necesidades que requerimos, sin emabrgo en algunas ocasiones estas requieren aprovacion

Para eliminar un Plano tecnico tenemos que desasignarlo y posteriormente eliminarlo

##### Cumplimiento
En este apartado podemos ver que directivas se estan cumpliendo y cuales no
 
##### Correción
 Nos ayuda los errores y poder corregir los mismos

##### Eventos
Podemos ver cuando no se cumplio una reglas o cuando si

- ##### Etiquetas
	- Sirven para los cumplimientos de las reglas.
	- Nos permite dar más informacion a las personas que los usaran.
	- Tambien sirven para buscar los recursos más facil
	- Para sacar reportes de costos

###### Ambito
Es un grupo de recursos, suscripcion, recursos o grupo de administracion

##### Directiva
Una directiva debe de tener lo siguiente:
- Ubicacion de defincion
	- Seleccionamos en donde queremos aplicar la directiva, en nuestra suscripcion  o bien o todo las cuentas que esten relacionadas
- Nombre 
- Definicion
	- Lo que hara esta regla, como evitar crear un recursos en fuera de cierta region

Podemos modificar el codigo de la directiva 

Podemos asignarla en un ambito
- Nuestra Suscripcion
- Grupo de recursos

**Exclusiones**
- Podemos excluir una regla para que a cierto recurso no se le aplique la regla 

En la definicion, decidimos que queremos permitir o negar. 

**Parametros**
- Seleccionamos las ubicaciones permitidas 


**PRACTICA 28:00**

**Inciativa**

Podemos crear una iniciativa desde Directory, una iniciativa es un conjunto de reglas o directivas. Podemos colocar muchas directivas de golpe

### BluePrints
Un BluePrint es un conjunto de Iniciativa, podemos controlar mejor los usuarios y la nube

Podemos implemntar blue prints para cumplimiento de normas legales

Existen 3 tipos de bloqueos como:
- Solo lecutra
- No eliminar
- No bloquear 

Podemos crear valores predefinidos para que cuando se cumple o se viole una directiva se realice una accion.

 Podemos asignar el plano tecnico o blueprint puede ser asignado a toda una suscripcion o un grupo de recursos

Para borrar un plano tenemos que desasignarlo y despues eliminarlo


### Grupo de recursos

Podemos compartir grupo de recursos desde la configuracion del grupo de recusos en la seccion de acceso, ahi seleccionamos los permisos que le queremos dar como podria ser lector, administrador, propietaro, etc. Despues agregamos al usuario que incluiremos al grupo de recursos.

Existen distintos roles que se adaptan a lo que necesitamos o en su defecto podemos crear un rol para especificar a lo que queremos que tengan acesso los usuario asignados.

Con los roles podemos monitorear las acciones de los usuarios dentro de nuestro grupo de recursos

Asi podemos trabajar en conjunto con nuestros compañeros o colaboradores


**Etiqueta** 
- Buscar más facilimente recursos
- Informacion para las personas que usaran el servicio
- Reportes de costo por etiqueta
- Cumplimiento de las reglas

Cost manager solo para una cuenta empresarial o  bien cuando se paga

### Calculadora TCO (total cost of ownership)
Es una calculadora Sirve para comparar el costo de un entorno privado y el costo en Azure, en la nube

### Calculadora de Precios
Sirve para hacer presupuestos unicamente de la nube, los recursos de azure como blob, functions, VM, etc.

**Reduccion de Costos*
- Cambiar de region
- Reduciendo el uso de los recursos 
- Quitar recursos que no se utilizan
- Cambiando el S.O. podemos ahorrar, en el caso de las maquinas virtuales o bien si aplica el recurso
- Teniendo las licencias
	-  licencia de Windows Server 
	- Licencias de DataBase
- Reservando el recurso de azure por 1 o 3 años (Si aplica el recurso)

### Actualizaciones de Azure
Existen actualizaciones que azure va incorporando a sus servicios pero estas tienen tres estado de las actualizaciones:

-  Ya disponible
	- Puede tener unos errores, pero ya tienen SLA y costo
-  En version preliminar
	- Podemos probar la beta pero puede tener errores
-  En Desarrollo
	- Anunciado pero no se puede usar

Preview Azure aqui estan las versiones preliminares de Azure

### Azure Status
Son los status de los servicios de Azure, de todas las regiones de azure

Nos muestras si algun servicio esta fallando, podemos ver de manera rapida si un recurso esta fallando pero para uno más especifico utilizamos **Service Health**




