from flask import request
import socket
from datetime import datetime

from ..models.Visitas import Visitas

class DashboardController:
    
    def contar_visita(self):
        data = datetime.now()
        data_visita = data.strftime('%d/%m/%Y')
        ip_visita = socket.gethostbyname(socket.gethostname())

        visita = Visitas(ip_visita=ip_visita, data_visita=data_visita)
        db.session.add(visita)
        db.commit()

    def contador_visitas_dia(self):
        pass

    def contato_visitas_mes(self):
        pass

    def contador_visitas_total(self):
        pass

