from ..app import db

class Visitas(db.Model):
    __tablename__ = 'visitas'

    id_visita = db.Column(db.Integer, primary_key=True)
    ip_visita = db.Column(db.String(32))
    data_visita = db.Column(db.Date)

    def __init__(self, ip_visita, data_visita):
        self.ip_visita = ip_visita
        self.data_visita = data_visita