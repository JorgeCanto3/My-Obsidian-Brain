# Azure Database for PostgreSQL
Azure Database for PostgreSQL es un servicio de base de datos relacional con la nube. El software de servidor se basa en la versión de la comunidad del motor de base de datos de PostgreSQL de código abierto.

Azure Database for PostgreSQL ofrece las siguientes ventajas: 

- Alta disponibilidad integrada
- Precios sencilloy flexibles
- Escalado o reduccion vertical segun lo necesario.
- Copias de seguridad automatica
- Seguridad y cumplimiento a nivel empresarial para proteger la información. _Esta seguridad abarca el cifrado de datos en el disco y el cifrado SSL entre la comunicación entre cliente y servidor._

**Un solo servidor**

Implementar un solo servidor nos ofrece casi las mismas ventajas que se comentan con anterioridad pero con la ventaja de Supervision y alertas para evaluar el servidor.

Ofrece tres planes de tarifa:
- Básico
- De uso general
- Optimizado para memoria.
Cada uno esta pensado para admitir distintas cargas de trabajo en las bases de datos

Ya que no requieren de gran administacion se puede centrar en el desarallo de las aplicaciones.

**Hiperescala (Citus)**

Escala de manera horizontal las consultas entre varias maquinas mediante el particionamiento. Su motor de consultas paraleliza las consultas SQL entrantes en estos servidores para agilizar las respuestas en conjuntos de datos grandes. 

Suele ser usada para aplicaciones que requieren de mayor escala y mejor rendimiento.

Admite aplicaciones multiinquilino, análisis operativos en tiempo real y cargas de trabajo transaccionales de alto rendimiento