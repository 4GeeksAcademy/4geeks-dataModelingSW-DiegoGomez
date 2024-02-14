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

#Para las propiedades de Character y Planet, me he basado en mi proyecto de Star Wars, simulando
#la creación de una base de datos para los campos que yo quise mostrar en el proyecto
    
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
    # El id de homeworld (planeta) que se muestra es una foreignkey que referencia el id
    # de la tabla planet. Esta relación es de uno a uno, es decir, cada personaje individualmente
    # pertenece a un planeta concreto, aunque varios personajes pueden pertenecer a un mismo planeta.
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
    # esta relación es de uno a muchos, de forma que un usuario puede tener varios favoritos.
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    # Para gestionar que se almacena en favoritos, este campo almacena el tipo de favorito (planet o character).
    favorite_type = Column(String(50)) 
    favorite_id = Column(Integer)

## Renderizar el diagrama de la base de datos
render_er(Base, 'diagram.png')
