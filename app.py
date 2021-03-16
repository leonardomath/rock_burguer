from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'storage.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    return '<h1>index</h1>'

@app.route('/reservar_mesa', methods=['POST'])
def reservar_mesa():
    pass

@app.route('/trabalhe_conosco', methods=['POST'])
def salvar_contato():
    pass

app.run()