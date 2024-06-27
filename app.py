from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import create_app, db
from app.models.usuarios import Usuario

# Crear la aplicación usando la factory function
app = create_app()

# Ruta principal para el login
@app.route('/')
def inicio():
    return render_template('login.html')

# Ruta para procesar el formulario de login
@app.route('/form', methods=['GET', 'POST'])
def loginForm():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        # Verificar las credenciales contra la base de datos
        user = Usuario.query.filter_by(nombre_usuario=usuario).first()
        
        if user and check_password_hash(user.contraseña, contraseña):
            # Credenciales válidas, redirigir a la página de reservas
            return redirect(url_for('reservas'))
        else:
            # Credenciales incorrectas
            return render_template('login.html', msg="Login Incorrecto")
    else:
        return render_template('login.html')

# Ruta para la página de reservas
@app.route('/reservas')
def reservas():
    dia = 23  # Este valor debería ser dinámico
    return render_template('reservas.html', dia=dia)

# Ruta para la página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre_usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        # Verificar si el usuario ya existe
        if Usuario.query.filter_by(nombre_usuario=nombre_usuario).first():
            return render_template('register.html', msg="Usuario ya existe")
        
        # Crear un nuevo usuario
        hashed_password = generate_password_hash(contraseña, method='pbkdf2:sha256')
        nuevo_usuario = Usuario(nombre_usuario=nombre_usuario, contraseña=hashed_password)
        
        # Añadir el nuevo usuario a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        # Redirigir a la página de reservas después del registro
        return redirect(url_for('reservas'))
    
    return render_template('register.html')

if __name__ == "__main__":
    # Ejecutar la aplicación en modo depuración
    app.run(debug=True, host='0.0.0.0', port=5000)
    print("Aplicación en ejecución")