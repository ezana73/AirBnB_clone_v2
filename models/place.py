#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', cascade='all, delete',
                               backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place')
    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            reviewList = []
            reviewDict = storage.all(Review)
            for review in reviewDict.values():
                if review.place_id == self.id:
                    reviewList.append(review)
            return reviewList

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            amenityList = []
            for amenity in self.amenity_ids:
                if amenity == self.id:
                    amenityList.append(amenity)
            return amenityList

        @amenities.setter
        def amenities(self, value):
            if type(value) is object:
                if value.__class__.__name__ == 'Amenity':
                    self.amenity_ids.append(value.id)
