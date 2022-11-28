from flask_appbuilder import Model
from sqlalchemy import Column, Integer, Float

class Cisla(Model):
    id = Column(Integer, primary_key=True)
    cislo = Column(Float)

    def __repr__(self):
        return self.name
