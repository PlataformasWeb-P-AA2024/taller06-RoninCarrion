from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from genera_base import Paises

import json

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basepaises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

url = "https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json"
response = requests.get(url)
datos_json = response.json()
documentos = datos_json

for d in documentos:
    print(d)
    print(len(d.keys()))
    p = Paises(nombrePais=d['CLDR display name'], capital=d['Capital'],  continente=d['Continent'], \
            dial=d['Dial'], geoname_id=d['Geoname ID'], itu=d['Geoname ID'],lenguajes=d['Languages'], \
            tipoEstado=d['is_independent']  )
    session.add(p)

# confirmar transacciones

session.commit()
