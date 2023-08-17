from configs.config import *

class Jogada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tempo = db.Column(db.Float)

    def __str__(self):
        return f"ID: {self.id}, tempo: {self.tempo}"

    def json(self):
        return {
            "id": self.id,
            "tempo": self.tempo
        }