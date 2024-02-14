import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

# Defino la base de datos en esta linea, de forma que las clases que lleven Base como parámetro
#estarán dentro de la base de datos
Base = declarative_base()

# Clase User
class User(Base):
    # Nombre de la tabla
    __tablename__ = 'user'
    # Campos
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    # Relación con la tabla de favoritos
    favorites = relationship("Favorite")

# Clase User
class Character(Base):
    # Nombre de la tabla
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    height = Column(Integer)
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    # Relación con la tabla de planetas
    homeworld = relationship("Planet")

class Planet(Base):
    # Nombre de la tabla
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(Integer)
    diameter = Column(Integer)
    gravity = Column(String(250))
    climate = Column(String(250))
    orbital_period = Column(Integer)
    surface_water = Column(Integer)
    rotation_period = Column(Integer)

class Favorite(Base):
    # Nombre de la tabla
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    # El id de usuario que se muestra es una foreignkey que viene del id que tiene la tabla usuario
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favorite_type = Column(String(50)) 
    favorite_id = Column(Integer)

## Renderizar el diagrama de la base de datos
render_er(Base, 'diagram.png')
