#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', cascade='all, delete', backref='states')
    else:
        @property
        def cities(self):
            from models.city import City
            from models import storage
            cityList = []
            cityDict = storage.all(City)
            for city in cityDict.values():
                if city.state_id == self.id:
                    cityList.append(city)
            return cityList
