import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# Relación uno a uno: Un usuario puede crear un username o cuenta en Instagram
class Person(Base):
    __tablename__ = 'persona'
    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))

# Uno a muchos: Uno usuario creado o username comienza a seguir muchos otros usuarios o Followings
class Username(Base):
    __tablename__ = 'username'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Followings(Base):
    __tablename__ = 'followings'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))

# Muchos a uno: comentarios: pueden haber muchos comentarios hacia un usuario
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('child.id'))
    child = relationship("Child")

class userN(Base):
    __tablename__ = 'usern'
    id = Column(Integer, primary_key=True)

#Muchos a muchos: El usuario puede tener muchos followers y hacer muchos followings
class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e