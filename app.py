from flask import Flask, render_template, request, redirect, session, flash, url_for
import mysql.connector
from mysql.connector import Error
import threading
import webbrowser
import smtplib
from email.message import EmailMessage
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesario para flash

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        # Aquí iría el guardado en base de datos, etc.
        flash("Este mensaje muestra que se envió el formulario exitosamente.")
        return redirect(url_for('home'))  # Redirige a home.html
    return render_template('agregar.html')

# Conexión a la base de datos con puerto 3307
try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="vt3525holapt",
        database="gestor_persona"
    )
    print("Conexión exitosa.")
except Error as err:
    print("Error al conectar:", err)
    input("Presiona Enter para salir...")
    exit()

cursor = conexion.cursor()

app = Flask(__name__)
app.secret_key = 'clave_segura_para_sesiones'

# Función para enviar correo
def enviar_correo_registro(datos):
    msg = EmailMessage()
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cuerpo = f"""
    Nuevo registro recibido:

    Hora: {hora}
    Cédula: {datos[0]}
    Nombre: {datos[1]}
    Teléfono: {datos[2]}
    Dirección: {datos[3]}
    Estrato: {datos[4]}
    EPS: {datos[5]}
    Fecha: {datos[6]}
    Correo: {datos[7]}
    """
    msg.set_content(cuerpo)
    msg['Subject'] = 'Nuevo registro en la plataforma'
    msg['From'] = 'wildermanuel777@gmail.com'
    msg['To'] = 'wildermanuel777@gmail.com'

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('wildermanuel777@gmail.com', 'fomr ugww eprp pgtw')
            smtp.send_message(msg)
            print("Correo enviado con éxito.")
    except Exception as e:
        print("Error al enviar correo:", e)

@app.route('/')
def home():
    return render_template("inicio.html")

@app.route('/formulario')
def formulario():
    return render_template("home.html")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']
    if usuario == "wilder manuel" and contrasena == "vt3525holapt":
        session['usuario'] = usuario
        return redirect('/index')
    else:
        flash("Credenciales incorrectas", "error")
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    flash("Sesión cerrada correctamente.", "mensaje")
    return redirect(url_for('home'))

@app.route('/index')
def index():
    if 'usuario' in session:
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
        return render_template("index.html", personas=personas)
    flash("Debes iniciar sesión para ver esta página.", "error")
    return redirect(url_for('home'))

@app.route('/agregar', methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        datos = (
            request.form["cedula"],
            request.form["nombre"],
            request.form["telefono"],
            request.form["direccion"],
            request.form["estrato"],
            request.form["eps"],
            request.form["fecha"],
            request.form["correo"]
        )
        print("Datos recibidos:", datos)

        try:
            cursor.execute("""
                INSERT INTO personas 
                (cedula, nombre, telefono, direccion, estrato, eps, fecha, correo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, datos)
            conexion.commit()
            enviar_correo_registro(datos)
            flash("Datos registrados correctamente.", "mensaje")
            print("Registro guardado.")
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "error")
            print("ERROR AL INSERTAR:", err)

        return redirect(url_for('formulario'))

    return render_template("agregar.html")

@app.route('/eliminar/<string:cedula>')
def eliminar(cedula):
    if 'usuario' not in session:
        flash("No tienes permisos.", "error")
        return redirect(url_for('home'))
    cursor.execute("DELETE FROM personas WHERE cedula = %s", (cedula,))
    conexion.commit()
    flash("Registro eliminado.", "mensaje")
    return redirect(url_for('index'))

if __name__ == '__main__':
    def abrir_navegador():
        webbrowser.open_new("http://127.0.0.1:5000")
    threading.Timer(1, abrir_navegador).start()
    app.run(debug=True)