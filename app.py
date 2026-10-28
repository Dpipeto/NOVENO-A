from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/justificacion')
def justificacion():
    return render_template('justificacion.html')


@app.route('/crisisdeextincion')
def crisisdeextincion():
    return render_template('crisis_extincion.html')


@app.route('/reciclaje')
def reciclaje():
    return render_template('reciclaje.html')


@app.route('/tips')
def tips():
    return render_template('tips.html')


if __name__ == '__main__':
    # Solo para probar en el computador. En Render la app se ejecuta con gunicorn.
    app.run(debug=True)
