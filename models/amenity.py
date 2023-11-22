#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import environ
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """ class amenity """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    
    if environ.get('HBNB_TYPE_STORAGE') =='db':
        place_amenities = relationship('Place', secondary="Place_amenity",
                                       back_populates="amenities")
    else:
        place_amenities = []
