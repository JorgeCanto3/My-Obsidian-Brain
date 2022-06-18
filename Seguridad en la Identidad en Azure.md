# Seguridad en la Identidad en Azure

La _identidad_ se ha convertido en el nuevo límite de seguridad principal. Para mantener el control de los datos, es fundamental que el usuario demuestre con exactitud que es un usuario válido del sistema y que cuenta con un nivel de acceso adecuado.

_Los ataques se dirigen más a la capá de identidad que de red_

Existen dos conceptos fundamentales para entender sobre el acceso y la identidad:

- La autenticación (AuthN)
- La autorización (AuthZ)

_La autenticación y la autorización admiten todo lo demás que se produzca. Aparecen de manera secuencial en el proceso de identidad y acceso_

<h2> Autenticación

Es el proceso donde de establecimineto de la identidad de una persona o servicio que quiere acceder a un recurso. 

Se solicitan credenciales legítimas y proporciona la base para la creación de una entidad de seguridad para el control de identidad y de acceso.

Cuando se piden las credenciales se identifica si el usuario es quien dice ser

<h2> Autorización 

Es el proceso de establecer el nivel de acceso que tienen una persona o un servicio autenticados. especifica a que datos. Ademas se especifica a qué datps puede acceder y que puede hacer con ellos


![[Pasted image 20220618005414.png]]


Con la tarjeta se representa la identridad y con esa infromacion la autorización define a qué tipos de aplicaciones, recursos y datos puede acceder el usuario.


## Servicios de Azure para identidad 

Para la seguridad y identificacion de identidad de los usuarios en Azure cuenta con 

- [[Azure Active Directory]]

Sin embargo tambien existe 
[[Active Directory ]] que se relazciona mucho con  Azure Directory

**Diferencia de Active Directory y Azure AD**

Ejecutado [[Active Directory]] en Windows Server proporciona un servicio de administración de acceso e identidad administrado por nuestra organizacion. 

En cambio Azure AD es un servicio de administración de acceso e identidades basado en la nube de Microsoft.

Ademas nosotros controlamos las cuentas de identidad y microsoft garantiza que el servicio este disponible de manera global 

Si usamos [[Active Directory]] de forma local Microsoft no detecta los intentos de acceso pero si conectamos [[Active Directory]] con [[Azure Active Directory]] se pueden detectar los intentos de acceso  sospechosos para proteger el entorno sin costo adicional


## Inicio de sesion único (SSO)

Permite a los usuario inicar sesión una vez y utilizar esa credencial para acceder a varios recursos y aplicaciones de distintos proveedores

Con este modelo es más facil administrar las contraseñas para los usuarioas como para los encargados de administrarlas para poder bloquear cuentas o restablecer

Con SSO, solo se debe recordad un ID y contraseña. El acceso a las aplicaciones se concede con una única identidad que se asocia a un usuario, simplificando el modelo de segurida

### Conexion de [[Active Directory]] con [[Azure Active Directory]]

Esta conexion proporciona una experiencia de identidad coherente a los usuarios.

El metodo más popular es con Azure AD conncect.

Connect sincroniza las identidades de usruaio entre la instalcion local de AD y Azure AD. Connect sincroniza los cambios entre ambios sistemas de identidades para poder uasr caracterristicas como SSO o autentiticación mutlifactor.

_Diagrama de como encaja Connect con AD local y Azure AD_

![[Pasted image 20220618024719.png]]


## Autenticacion Multifactor (AM)

Es un proceso en el que durante el inicio de seión de un usuario se solicita una forma adicional de identificación. Como teléfono móvil o lector de huellas dactilares

La AM proporciona seguridad adiconal a las identidades ya que se requieren dos o más elementos para una autenticación completo

Los elementos se dividen en tres categorías.

- Algo que el usuario conoce
	- Contraseña o correo

- Algo que el usuario
	-Codigo que se envia al movil del usuario

- Algo que el usuario es
	- Datos biometricos

![[Pasted image 20220618031537.png]]

Es una buena opcion para aumentar la seguridad, asi si se realiza un ataque, el atacante requerira más que solo la contraseña

## Azure AD Multi-Factor Authentication

Servicio de microsoft que proporciona funcionalidades de autenticación multifactor. Permite que los usuarios elijjan una forma adicional de autenticación ante el incio de sesion.

Este servicio se proprociona en los siguientes servicios

- **Azure Active Directory**
	
	-  En la edicion gratituda de Azure AD se habilita el mutli-factor para los administradores con el nivel de acceso de administrador global. Tambien lo podemos aplicar a todos los usuarios solo mediante Microsoft Authenticator
	
	-  La version premium  permite una configuración exhaustiva y detallada de Multi-Factor a través de directivas de acceso condicional

- **Autenticación multifactor para Office 365**
	- Esta suscripcion incluye un subconjunto de funcionalidades de Multi-Factor

----------
## Acceso Condicional

Es una herramietna que usa Azure AD para permitir o denegar el acceso a los recursos en funcion de señales de identidad. Señales como quien es, donde se encuentra y el dispositivo de acceso

Con esto los Administradores de TI pueden:

-  permitir a los usuarios ser productivos en cualquier momento y lugar;

-  proteger los recursos de la organización.

![[Pasted image 20220618032554.png]]

_Dependiendo de las señales sera si se pedira un 
 segundo factor de autenticacion_

### Cuando usar

Util para 

 - Requerir la autenticación multifactor para acceder a una aplicación.
 
	 - Podemos configurarla para ciertos o usuarios o por el tipo de red

- Para requerir el acceso a los servicios solo a través de aplicaciones cliente aprobadas. 

- Podemos exigir que los usuarios accedan a la aplicación solo desde dispositivos administrados.


_Disponibel con  licencia de Azure AD Premium P1 o P2_

-------------

