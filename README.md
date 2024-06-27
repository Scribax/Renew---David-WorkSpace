## Últimas Actualizaciones ##

## Actualización 14:36, 27 Junio 2024

**Actualización del .gitignore:** Se ha actualizado el archivo `.gitignore` para ignorar correctamente los archivos y carpetas que no deben estar en el repositorio, como el entorno virtual (`venv/`) y archivos sensibles (`*.env`).

## Actualización 22:30, 26 Junio 2024

### Cambios Recientes

**Creación de Usuarios:**

- **Archivos Modificados:** `login.html`, `register.html`, `app.py`, `app/__init__.py`.
- **Descripción:** Se implementó la funcionalidad para permitir la creación de un nuevo usuario en caso de que el cliente no tenga uno existente.

**Persistencia de Datos:**

- **Problema Resuelto:** Anteriormente, si el servidor se detenía o fallaba, la base de datos se reiniciaba y perdía los datos. Ahora, los usuarios y contraseñas se almacenan de manera persistente en una base de datos, asegurando la integridad de la información incluso después de reiniciar el servidor.

**Mejoras Visuales:**

- **Archivos Modificados:** `register.html`, `login.html`.
- **Descripción:** Se realizaron mejoras visuales en las páginas de registro e inicio de sesión para una experiencia de usuario mejorada.

**Actualización de Requisitos:**

- **Archivo Modificado:** `requirements.txt`.
- **Descripción:** Se actualizó la lista de dependencias del proyecto para reflejar los cambios recientes.

---

## Instrucciones para Configuración Inicial

### Clonar el Repositorio

```bash
git clone https://github.com/Scribax/Renew---David-WorkSpace.git
cd Renew---David-WorkSpace

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Configurar Variables de Entorno
Crear un archivo .env en la raíz del proyecto y agregar las variables necesarias.

```bash
flask run
```


