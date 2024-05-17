from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Paises

import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///countriesdb.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

datos = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
# archivo = request.get("------------------.json")
datos = datos.json()
#datos_json =  json.load(archivo) # paso los datos del archivo a json
# archivo.json()
#documentos = datos_json["docs"]

for country in datos:
    print(country)
    print(len(country.keys()))
    p = Paises(nombrePais=country['CLDR display name'], capital=country['Capital'],
                contienente=country['Continent'], \
            dial=country['Dial'],
            geoname_id=country['Geoname ID'],
            itu=country['ITU'],
            lenguajes=country['Languages'],
            tipoEstado=country['is_independent'])
    session.add(p)
# confirmar transacciones

session.commit()
