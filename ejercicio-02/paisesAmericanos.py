from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_base import Paises
from genera_base import engine

Session = sessionmaker(bind=engine)
session = Session()



# Uso de or_

paisesCon = session.query(Paises).filter(or_(Paises.continente=="NA", Paises.continente=="SA"))
for pais in paisesCon:
    print(f"ID: {pais.id}, Nombre: {pais.nombrePais}, Capital: {pais.capital}, Continente: {pais.continente}, Dial: {pais.dial}, Geoname ID: {pais.geoname_id}, ITU: {pais.itu}, Lenguajes: {pais.lenguajes}, Tipo de Estado: {pais.tipoEstado}")

