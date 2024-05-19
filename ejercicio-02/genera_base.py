from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Se genera el enlace al gestor de base de datos
# para el ejemplo se usa la base de datos SQLite
engine = create_engine('sqlite:///basepaises.db')

Base = declarative_base()

class Paises(Base):
    __tablename__ = 'paises'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombrePais = Column(String, nullable=True)
    capital = Column(String, nullable=True)
    continente = Column(String, nullable=True)
    dial = Column(String, nullable=True)
    geoname_id = Column(String, nullable=True)
    itu = Column(String, nullable=True)
    lenguajes = Column(String, nullable=True)
    tipoEstado = Column(String, nullable=True)

Base.metadata.create_all(engine)
