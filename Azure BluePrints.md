# Azure BluePrints

## Definicion 
Azure Blueprints puede definir un conjunto repetible de herrramientas de gobernanza y recursos de Azure estándar que una organización necesita

Pensemos en BluePrints como plantillas de reglas que podemos implementar en distintas suscripciones para agilizar el trabajo

Azure BluePrints organiza la implementacion de varias plantilla de recursos y de artefacto como los siguientes:

-   Asignaciones de roles
-   Asignaciones de directivas
-   Plantillas de Azure Resource Manager
-   Grupos de recursos

## Implementacion

Para implementar un proyecto tenemos que realizar los sieguientes pasos:

1.  Crear una instancia de Azure Blueprints
2.  Asignar ese plano técnico
3.  Llevar un seguimiento de las asignaciones del plano técnico


La relación entre la definición del plano técnico (lo que debe ser implementado) y su asignación (lo que se ha implementado) permanece. 
Azure crea un registro que asocia un recurso con el plano técnico que lo define, y gracias a esta conexión podemos realizar el seguimiento y la auditoría de nuestras implementaciones.

## Artefactos 

Los artefactos son componetnes de la definicion en un plano técnico

Es posible que los artefactos no tengan parámetros adicionales (configuraciones)

Estos pueden contener uno o más parámetros que se pueden configurar