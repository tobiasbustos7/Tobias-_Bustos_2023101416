from flask import Flask, render_template, request, redirect, url_for, session
from db_connection import get_db_connection
import mysql.connector

app = Flask(__name__)
app.secret_key = 'ganaderia_secret_key'

CATTLE_LOTS = [
    {
        "type": "Ternero/a",
        "description": "Bovino joven, generalmente al pie de la madre. Ideal para crecimiento.",
        "quantity": 150,
        "price": "Gs. 2.500.000 / cabeza",
        "image": "ternero.jpg"
    },
    {
        "type": "Novillito",
        "description": "Macho castrado de destete hasta aproximadamente los dos años. Excelente potencial de engorde.",
        "quantity": 80,
        "price": "Gs. 3.800.000 / cabeza",
        "image": "novillito.jpg"
    },
    {
        "type": "Novillo",
        "description": "Macho castrado de más de dos años. Listo para faena o terminación.",
        "quantity": 50,
        "price": "Gs. 4.500.000 / cabeza",
        "image": "novillo.jpg"
    },
    {
        "type": "Vaquillona",
        "description": "Hembra desde el destete hasta su primera parición. Genética de alta calidad.",
        "quantity": 120,
        "price": "Gs. 3.500.000 / cabeza",
        "image": "vaquillona.jpg"
    },
    {
        "type": "Vaca",
        "description": "Hembra adulta. Lotes de cría o descarte.",
        "quantity": 200,
        "price": "Gs. 4.000.000 / cabeza",
        "image": "vaca.jpg"
    },
    {
        "type": "Toro",
        "description": "Macho entero (no castrado). Reproductores seleccionados.",
        "quantity": 15,
        "price": "Gs. 8.000.000 / cabeza",
        "image": "toro.jpg"
    },
]

@app.route('/')
def home():
    return redirect(url_for('dashboard'))

# Ruta para el dashboard
@app.route('/dashboard')
def dashboard():
    message = session.pop('flash_message', None)
    message_type = session.pop('flash_message_type', None)
    return render_template('index.html', lots=CATTLE_LOTS, message=message, message_type=message_type)

# Ruta para el formulario de contacto
@app.route('/contact')
def contact():
    return render_template('contact.html', lots=CATTLE_LOTS)

# Ruta para procesar el formulario de contacto
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    full_name = request.form['full_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    preferred_time = request.form['preferred_time']
    cattle_type = request.form['cattle_type']

    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO contact_requests (full_name, email, phone_number, preferred_time, cattle_type)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (full_name, email, phone_number, preferred_time, cattle_type))
        conn.commit()

        session['flash_message'] = "¡Solicitud enviada con éxito! Nos pondremos en contacto contigo pronto."
        session['flash_message_type'] = 'success'
        
    except mysql.connector.Error as err:
        print(f"Error de base de datos: {err}")
        session['flash_message'] = "Hubo un error al procesar tu solicitud. Inténtalo de nuevo."
        session['flash_message_type'] = 'error'
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')