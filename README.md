# Temporizador

---
# Descripción
Aplicación web que pérmite configurar una sesión de entrenamineto basada en el concepto de Every Minute On The Minute.

---

Participantes:
1. Carlos Eduardo López
2. Cristian Gutierrez Gomez
3. Jairo Murcia Ardila

---
## Componentes

La base de datos para usuario, la página para registrarlos ,entrar a una sesión, salir de ella, todas las validaciones ya estan hechas y una plantilla para los scripts html.

El script form.py se encarga registrar y logear a los usuarios y procesar que los datos sean correctos , esta trabaja en conjunto con el script models.py que se encarga de crear las bases de datos y sus tablas.

Además el uso del framework Flask que permite el uso de plantillas base en las vistas. Para esta primera versión solo se tiene una, base.html, esto nos permite crear una estructura para crear más rápido páginas que van a tener un mismo estilo y presentación. Por otro lado el framework posee algo llamado Blueprints, los cuales son una especie de componentes, que se pueden usar en la aplicación principal, independiente mente de los demás. Por ejemplo, si un gimnasio quisiera agregar la funcionalidad del temporizador a su página, sería muy sencillo agregarlo como un Blueprint, teniendo en cuenta que esté desarrollada en el mismo framework.


