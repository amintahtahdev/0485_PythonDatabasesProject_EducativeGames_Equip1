import json
import os
from .user import User
from extensions import db

class Storage:
    def __init__(self):
        pass

    def load_users(self):
        # Ara llegim de la base de dades MariaDB
        return User.query.all()

    def get_user(self, username):
        # Busca un usuari a la BBDD MariaDB
        return User.query.filter_by(username=username).first()

    def add_user(self, new_user):
        # Afegeix un nou usuari a la BBDD MariaDB
        db.session.add(new_user)
        db.session.commit()

    def save_game_result(self, username, game_name, game_type, points):
        # Per ara mantenim la part de puntuacions separada o segons es necessiti,
        # però l'usuari el busquem a la BBDD
        current_user = self.get_user(username)
        if not current_user:
            return 0
        
        # Aquí aniria la lògica de guardar puntuacions si es migren també
        return 0