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

countries_languages = session.query(Paises.nombrePais, Paises.lenguajes).all()
for country, languages in countries_languages:
    print(f"País: {country}, Lenguajes: {languages}")
