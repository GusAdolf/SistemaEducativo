#IMPORTAR LIBRERIA PARA USAR FRAMEWORK FLASK
from flask import Flask
from flask import render_template
import os
from flask import request
import backend
##llamado a flask
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'img')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER
##servicio web


@app.route('/', methods = ["GET","POST"])
def home():
    fondoP = os.path.join(app.config['UPLOAD_FOLDER'], 'cat-4.jpg')
    return render_template('index.html',fondo=fondoP)

@app.route('/cursos', methods = ["GET","POST"])
def cursos():
    progra = os.path.join(app.config['UPLOAD_FOLDER'], 'progra.jpeg')
    ml = os.path.join(app.config['UPLOAD_FOLDER'], 'ml.png')
    va = os.path.join(app.config['UPLOAD_FOLDER'], 'va.jpg')
    ig = os.path.join(app.config['UPLOAD_FOLDER'], 'ig.png')
    return render_template('cursos.html',progra=progra, ml=ml , va=va, ig=ig)

@app.route('/login', methods = ["GET","POST"])
def login():
    return render_template('login.html')
    
@app.route('/docentes', methods = ["GET","POST"])
def docentes():
    return render_template('docentes.html')
    
@app.route('/inscripciones', methods = ["GET","POST"])
def inscripciones():
    return render_template('insc.html')




##ejecutar el servicio web
if __name__=='__main__':
    #OJO QUITAR EL DEBUG EN PRODUCCION
    app.run(host='0.0.0.0', port=5000, debug=True)