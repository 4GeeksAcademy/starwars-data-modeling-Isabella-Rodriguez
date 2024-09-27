import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(6), nullable=False, unique=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    birth_year = Column(Integer)
    gender = Column(String(25))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    climate = Column(String(25))
    population = Column(Integer)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    User_from_id = Column(Integer, ForeignKey('users.id'))
    user_from = relationship(Users) 
    fav_planets_id = Column(Integer, ForeignKey('planets.id'))
    fav_planets = relationship(Planets)
    fav_characters_id = Column(Integer, ForeignKey('characters.id'))
    fav_planets = relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
