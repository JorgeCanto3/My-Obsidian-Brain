# Azure Dedicated Host
Es un servicio que proporciona servidores físicos dedicados para hosperad VM de Azure para Linux o Windows

_Ejemplo_ de las máquinas virtuales y los hosts dedicados y los grupos host.

![[Pasted image 20220616020006.png]]

_host dedicado_ se asigna a un servidor físico en un centro de datos de Azure.

Un _grupo host_ es una colección de hosts dedicados.

Ventajes de Dedicated host

- Visibilidad y control sobre la infraestructura de servidor de las MV's

-  Satisface los requisitos de cumplimiento mediante la implementación de las cargas de trabajo en un servidor aislado.

- Permite elegir el número de procesadores, capacidades de servidor, series de máquinas virtuales y tamaños de máquina virtual dentro del mismo host.


## Disponibilidad de Dedicated Host

Para lograr una alta disponibilidad, puede aprovisionar varios hosts en un _grupo host_ e implementar las máquinas virtuales en este grupo.

## Consideraciones sobre precios

Se cobra por host dedicado, con independencia de cuántas máquinas virtuales se implementen en él. El precio del host se basa en la familia de máquinas virtuales, el tipo (tamaño de hardware) y la región.