"# Renew---David-WorkSpace" 

No le den bola al venv, solo lo hice en mi pc, luego lo sacamos del original

//==========Actualización 22:30 26 Junio 2024==========//

Modifiqué los archivos login.html, register.html, app.py y en app/__init__.py para que se pudiera crear un usuario en el caso de que el cliente no tenga usuario.
Tambien corregí el bug de que si el servidor no iniciaba o se parara, la base de datos se borrara, ahora cada vez que el servidor se para y se vuelve a restablecer los 
usuarios y contraseñas se almacenan en un DB para ser utilizados a posterior.
Mejoras visuales en el apartado Register.html y Login.html
Tambien se actualizacó el Requirements.txt
