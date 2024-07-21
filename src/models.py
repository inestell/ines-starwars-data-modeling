import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    favorites = relationship("favorites", back_populates="user", uselist=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250), nullable=True)
    home_world = Column(Integer, ForeignKey('planets.id'))
    favorite_id = Column(Integer, ForeignKey("favorites.id"))
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    residents = relationship("Characters")
    favorite_id = Column(Integer, ForeignKey("favorites.id"))
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorites')
    favorite_characters = relationship("characters")
    favorite_planets = relationship("planets")
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
