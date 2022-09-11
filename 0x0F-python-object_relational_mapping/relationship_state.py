#!/usr/bin/python3
""" Definition of the State class. """

from relationship_city import City, Base

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Class State """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all,
                          delete-orphan')
