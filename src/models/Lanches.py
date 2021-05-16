from ..app import db

class Lanches(db.Model):
    __tablename__ = 'lanches'

    id_lanche = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.Text())
    foto = db.Column(db.String(100))

    def __init__(self, titulo, descricao, foto):
        self.titulo = titulo
        self.descricao = descricao
        self.foto = foto