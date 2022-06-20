# Azure Policy

Es un servicio de Azure que permite crear, asignar y administrar directivas que controlan o auditan recursos, estas directivas aplican distintas reglas en todas las configuraciones de los recursos para que se sigan cumpliendo con los estándares corporativos

### Definir directivas 

Se definien mediante el Azure Portal o herramienta de linea de comandos

![[Pasted image 20220618182815.png]]

Policy permite definir directivas **individuales** y en **grupos de directivas relacionadas**, a esto se le conoce como **iniciativa** 

**Policy** evalua los recursos y resalta aquellos que no cumplen las directivas que hemos creado, tambien puede impedir que se creen recursos no conformes

**Policy** Incluye definiciones de inciativas y directivas integradas  para categorías como Almacenamiento, Redes, Proceso entre otros. Con la defincion de directiva podemos permitir que se use determinados tamaños de SKU para las MV's. **Policy** ademas también evalúa y supervisa todas las máquinas virtuales que hay actualmetn en el entorno

En algunas ocasiones **policy** tambien puede corregir automaticamente los recursos y configuraciones no confromes para garantizar la integrida del estado de los recursos. Si algun recurso requiere la etiqueta **Policy** aplicara la etiqueta si se ha quitado

**La implementacion en Policy requiere tres tareas:**

1.  Crear una definición de directiva
	- Expresamos que se debe evaluar y qué acción realizar 
	- Ejemplos de directivas:
		- **SKU de maquinas virtuales permitidas**
		- **Ubicaciones permitidas**
		- **MFA debe estar habilitado en las cuentas con permisos de escritura de la suscripción**

2.   Asignar la definición a los recursos

- Es una definición de directiva que se aplica dentro de un ámbito específico.
	- El ambito puede ser un grupo de recursos, suscripcion, recursos, etc.
	- Los recursos secundarios heredaran las asginaciones de directivas

3.  Revisar los resultados de evaluación
	-  Se evalua con los recursos existentes, estos se marcan como conformes o no conformes. Con esto los que son no conformes podemos tomar acciones  


### Iniciativas en Policy

Las inciativas son una forma de agrupar las directivas relacionadas. La definicion de iniciativa contienen todas las definciones de directiva para facilitar el seguimietno deel estado de cumplimiento de cara a un objetivo mayor. En otras palabras contiene muchas reglas para poder hacer mas facil lograr nuestra meta y no tener problemas.

 Azure Policy incluye una iniciativa denominada **Habilitar la supervisión en Azure Security Center**, cuyo objetivo es supervisar todas las recomendaciones de seguridad disponibles para todos lor recursos de Azure en Security center. Esta inciativa contiene más de 100 definciones de directiva independientes

#### Asignacion de una iniciativa
Es un definicion de iniciativa que se asigna en un ámbito especifico de un grupo de admin, recursos o solo recursos, Igua que una directiva.

Podemos empezar con solo una directifva e ir aumentandolas con el tiempo