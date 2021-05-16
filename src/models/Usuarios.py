from ..app import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    id_usuario = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha