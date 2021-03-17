from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/postgres'
db = SQLAlchemy(app)

class Visitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_visita = db.Column(db.String(32), nullable=False)
    data_visita = db.Column(db.Date , nullable=False)