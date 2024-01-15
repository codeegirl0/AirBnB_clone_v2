#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State the class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getting list related city
            """
            city_listt = []

            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_listt.append(city)
            return city_listt
