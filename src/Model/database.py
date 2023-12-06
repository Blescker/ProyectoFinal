from sqlalchemy import create_engine, Column, Integer, Float, String 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

# Crear el motor de la base de datos (SQLite en este caso)
engine = create_engine('sqlite:///sueldos.db')

# Declarar la base para los modelos
Base = declarative_base()

class Sueldo(Base):
    __tablename__ = 'sueldos'

    id = Column(Integer, primary_key=True)
    nombre_trabajador = Column(String)
    sueldo_basico = Column(Float)
    dias_falta = Column(Integer)
    minutos_tardanza = Column(Integer)
    horas_extras = Column(Float)
    sueldo_neto = Column(Float)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()
