#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """class Place
    attr:
        city_id: the city id
        user_id: user id
        name: name input
        description: string  desc
        number_rooms: room in int
        number_bathrooms: bathrooms in int
        max_guest: max guest in int
        latitude: latitude in flaot
        longitude:  float
        amenity_ids: list Amenity id
        price_by_night:: price staying in int
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    amenity_ids = []


    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ Returns list of reviews.id """
            var = models.storage.all()
            thelist = []
            theresult = []
            for ky in var:
                review = ky.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    thelist.append(var[ky])
            for ele in thelist:
                if (ele.place_id == self.id):
                    theresult.append(ele)
            return (theresult)

        @property
        def amenities(self):
            """ returning list amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ adding amenity id to attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
