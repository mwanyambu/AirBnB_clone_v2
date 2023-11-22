#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Tablei
from sqlalchemy import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', Integer, ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', Integer, ForeignKey('amenities.id'),
                             primary_key=True))
class Place(BaseModel):
    """ A place to stay """
    if environ.get('HBNB_TYPE_STORAGE') == db:
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        lattitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan',
                               passive_deletes=True)
        amenity = relationship('Amenity', secondary="place_amenity",
                               back_populates="places")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """Returns a list of review instances"""
            from models.review import Review
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
        """ getter attr """
        return [amenity for aminity in models.storage.all(Amenity).values()
                if amenity.place_id == self.id]

        @amenities.setter
        def amenies(self, obj):
            """appends amenity_id to amenities.id """
            if not isinstance(obj, Amenity):
                return
            self.amenity_ids.append(obj.id)
