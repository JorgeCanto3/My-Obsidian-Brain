# Costos de Azure
Para conocer los costos podemos utilizar la calculadora para poder comprender los gastos y mantener el presupuesto.

## Calculadora

La Calculadora de TCO nos ayuda a costear los servicios de Azure con el tiempo. para ello podemos colocar los detalles de las cargas de trabajao en la calculadora y nos dira el costo medio sugeriod. Los costos incluyen la electicidad, mantenimiento de la red y el trabajo de TI Con un informe comprando las cargas

_Ejemplo_

![[Pasted image 20220619223224.png]]

## Funcionamietno 
El trabajo de la calculadore involucra 3 pasos:

1. Definir cargas de trabajo
	- Definimos  la infraestructura local en 4 categorias
		1. Servidores
		2. Bases de datos
		3. Storage
		4. Redes
2. Ajustar supuestos
-  Especificar si las licencias acutales están inscritas para Software Assurance, con esto podemos ahorrar licencias en Azur, Tenemos que ajujstar los valores a que coincidan con los costos de infraestructura local

3.  Visualización del informe
	- Elejimos un periodo de tiempo entre  1 y 5 años y la calculadora genera el informe y podemos ver una comparacion en paralelo de cada categoria
	 ![[Pasted image 20220619223731.png]]

## Suscripciones 

Una _suscripción_ de Azure le proporciona acceso a los recursos de Azure, como máquinas virtuales (VM), almacenamiento y bases de datos. Los tipos de recursos que use afectan a su factura mensual.

Azure ofrece las siguientes suscripciones

- **Evaluacion gratuita**

	- Proporciona 12 meses de servicios gratuitos populares, un crédito para explorar cualquier servicio de Azure durante 30 días y más de 25 servicios que siempre son gratis.
	
	- Despues del periodo de tiempo mencionado se desahbilitan los servicios de Azure

- **Pago por uso**
	- Permite pagar por lo que usa al conectar una tarjeta de crédito o débito a su cuenta.

- **Oferta para miembros**
	-  La pertenencia existente a determinados productos y servicios de Microsoft puede proporcionarle créditos para su cuenta de Azure y tarifas reducidas en los servicios de Azure.

## Adquirir servicios de Azure

Existen 3 formas

- **A través de un Contrato Enterprise**
- 
	- Mediante un contrato con Micorosfot nos comprometemos a gastar una cantidad predeterminada en los servicios de Azure durante un período de tres años. Normalmente, el precio de los servicios se paga anualmente.

- **Directamente desde la web**
	- Desde el Azure portal y se pagan los precios estandar

- **A través de un Proveedor de soluciones en la nube**

- Un Proveedor de soluciones es un partner de microsoft que ayuda a crear soluciones a partir de azure


## Factores que afectan al costo

### Tipo de recurso
Dependera del tipo de recurso que personalicemos


### Medidores de uso

Azure crea _medidores_ para realizar el seguimiento del uso de dicho recurso. Azure usa estos medidores para generar un registro de uso que posteriormente se usa para ayudar a calcular la factura.


### Uso de recursos
En Azure, siempre se le cobrará en función de lo que use.

### Tipos de suscripción de Azure

Algunos tipos de suscripciones de Azure también incluyen provisiones de uso que afectan a los costos.

### Localización 

La infraestructura de Azure se distribuye globalmente, lo cual permite implementar los servicios de forma centralizada o aprovisionar los servicios más cercanos al lugar donde los clientes los usan.

Distintas regiones pueden tener distintos precios asociados. Dado que las regiones geográficas pueden afectar al flujo del tráfico de red, el tráfico de red es también una influencia en el costo que se debe tener en cuenta.



## Costo Total

Para conocer el costo totall lo podemos obtener con la calculadora de precios de Azure.

La Calculadora de precios muestra los productos de Azure por categorías. Agregue estas categorías a su estimación y configúrelas según sus requisitos específicos. Luego recibirá un precio estimado consolidado, con un desglose detallado de los costos asociados a cada recurso que ha agregado a la solución

![[Pasted image 20220619225941.png]]

Las opciones que se pueden configurar en la Calculadora de precios varían entre productos, pero pueden incluir:
- **Región**
- **Nivel**
- **Opciones de facturación**
- **Opciones de soporte técnico**
- **Programas y ofertas
- **Precios de Desarrollo/pruebas de Azure****

## Consejos

tenga en cuenta detenidamente los productos, servicios y recursos que necesita. Lea la documentación correspondiente para comprender cómo se mide y factura cada una de las opciones.

 Usar Azure Advisor para supervisar la utilización, Azure Advisor identifica los recursos no utilizados o infrautilizados, y recomienda recursos no utilizados que se pueden quitar
![[Pasted image 20220619230525.png]]

 Usar límites de gasto para restringir los gastos

 Usar Reservas de Azure para pagar por adelantado. Reservas de Azure puede ahorrar hasta un 72 % en comparación con los precios de pago por uso.

Elegir regiones y ubicaciones de bajo costo

Uso de Microsoft Cost Management + Billing para controlar gastos

- Cost Management es un servicio gratuito que le ayuda a comprender su factura de Azure, administrar su cuenta y sus suscripciones, supervisar y controlar los gastos de Azure, y optimizar el uso de recursos.

Aplicar etiquetas para identificar a los propietarios de costos

 - _Las etiquetas_ ayudan a administrar los costos asociados a los distintos grupos de productos y recursos de Azure. Puede aplicar etiquetas a grupos de recursos de Azure para organizar los datos de facturación.

 Cambiar el tamaño de las máquinas virtuales infrautilizadas o apagarlas

Desasignar máquinas virtuales durante las horas de inactividad

- Recuerde que _desasignar_ una máquina virtual significa que ya no se ejecuta la máquina virtual, sino que se conservan los discos duros y los datos asociados en Azure.

Eliminar recursos no utilizados