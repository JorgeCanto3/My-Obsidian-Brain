# Azure Active Directory

Proporciona servicios de identidad que permiten a los usuario iniciar sesión y acceder tanto a las aplicaciones en la nube de Microsoft como en las aplicaciones que desarrollemos 

Azure AD adminite SSO (Inicio de sesión único)

### El uso de Azure AD es ideal para :

- **Administradores de TI**
	- Para controlar el acceso a las aplicaciones y los recursos de acuerdo a los requisitos empresariales

- **Desarrolladores de Aplicaciones**
	- Pueden agregar funcionalidad a las aplicaciones que compilan mediante un enfoque basado en estandares.Ej. podemos agregar SSO a una app

- **Usuarios**
	- Los usuarios pueden administrar sus identidades

- **Suscripciones de servicios en linea**
	- Los suscriptores de Microsoft y sus servicios utilizan Azure AD

### Servicios que proporciona Azure AD

- **Autenticacion:**
	-  Comprobación de la identidad para acceder a aplicaciones y recursos
	- Incluye el autoservicio de cambio de contraseñas, multifactor.

- **Inicio de sesión único:**
	- Los usuarios solo recuerdan un solo idenficador y una sola contraseña para varias aplicaciones

- **Administración de aplicaciones**
	- Podemos administrar las apps locales y en la nube.

- **Administración de dispositivos**
	- Permite administrar los dispositivos a través de herramientad como Microsoft Intune. Tambien se pueden limitar los intentos de acceso a solo aquellos que proceden de dispositovs conocidos


### Recursos que proteger con Azure AD

Ayuda a usuarios a acceder a recursos internos ccomo externos

- Externos
	- Microsoft Office 365, Azure Portal y miles de aplicaciones de SaaS

- Internos 
	- Aplicaciones de la red comporativa, la intranet y todas las apps desarrolladas por la organización

----
**Sesion con el Sherpa**

Es un servicio que crea y administra los usuarios, a que tienen acceso y que no tienen.

Controla el acceso a Azure pero podemos implementarlo con otras apps webs.

Este serivcio es Active Directory B2C podemos conectar aplicaciones externas para el login a nuestra pagina web como:

- Github
- Facebook
- Instagram
- Linkedin