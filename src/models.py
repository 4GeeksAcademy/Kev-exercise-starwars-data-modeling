import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(25), unique=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    favorites = relationship("Favorite", backref="user")
    logins = relationship("Login", backref="user")

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=True)
    character_img = Column(String(512), nullable=True)

    favorites = relationship("Favorite", backref="character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=True)
    planet_img = Column(String(512), nullable=True)

    favorites = relationship("Favorite", backref="planet")

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Login(Base):
    __tablename__ = "login"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.datetime.now())
    success = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
