from ..app import db

class Mensagens(db.Model):
    __tablename__ = 'mensagens'

    id_mensagem = db.Column(db.Integer, primary_key=True)
    nome_contato = db.Column(db.String(100))
    email_contato = db.Column(db.String(100))
    mensagem = db.Column(db.Text())

    def __init__(self, nome_contato, email_contato, mensagem):
        self.nome_contato = nome_contato
        self.email_contato= email_contato
        self.mensagem = mensagem