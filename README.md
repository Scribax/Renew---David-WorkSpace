Actualización 22:30, 26 Junio 2024

*Cambios Recientes*

Creación de Usuarios:

Archivos Modificados: login.html, register.html, app.py, app/init.py.
Descripción: Se implementó la funcionalidad para permitir la creación de un nuevo usuario en caso de que el cliente no tenga uno existente.

Persistencia de Datos:
Problema Resuelto: Anteriormente, si el servidor se detenía o fallaba, la base de datos se reiniciaba y perdía los datos. Ahora, los usuarios y contraseñas se almacenan de manera persistente en una base de datos. Esto asegura que la información se mantenga incluso después de reiniciar el servidor.
Mejoras Visuales:

Archivos Modificados: register.html, login.html.
Descripción: Se realizaron mejoras visuales en las páginas de registro y inicio de sesión para una mejor experiencia de usuario.
Actualización de Requisitos:

Archivo Modificado: requirements.txt.
Descripción: Se actualizó la lista de dependencias del proyecto para reflejar los cambios recientes.
Nota: El directorio venv es específico de la configuración local y se debe excluir del repositorio original.
