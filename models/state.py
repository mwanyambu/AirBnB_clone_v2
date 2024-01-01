#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: table name
        name: input name
        cities: relation to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models import storage
            """get all cities with the current state id
            from filestorage
            """
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
