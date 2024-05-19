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

countriesCha = session.query(Paises.nombrePais, Paises.capital).filter(
    Paises.nombrePais.like('%uador%') | Paises.capital.like('%ito%')
).all()
for country, capital in countriesCha:
    print(f"País: {country}, Capital: {capital}")