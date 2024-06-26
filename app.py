from flask import Flask, render_template, request
from app import create_app, db

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
        
        # Verificar las credenciales (esto es solo para ejemplo)
        if usuario == "admin" and contraseña == "1234":
            contador = 1234  # Este valor debería venir de la lógica de tu aplicación
            return render_template('reservas.html', varcontador=contador)
        else:
            return render_template('login.html', msg="Login Incorrecto")
    else:
        return render_template('login.html', msg="Login Incorrecto")

# Ruta para la página de reservas
@app.route('/reservas')
def reservas():
    dia = 23  # Este valor debería ser dinámico
    return render_template('reservas.html', dia=dia)

if __name__ == "__main__":
    # Ejecutar la aplicación en modo depuración
    app.run(debug=True, host='0.0.0.0', port=5000) 
    print("Aplicación en ejecución")
