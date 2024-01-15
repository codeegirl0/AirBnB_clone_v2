#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()

class BaseModel:
    """this is BaseModel class.
    Attr:
        id (sqlalchemy String): The bm id.
        created_at (sqlalchemy DateTime): The datetime at cre.
        updated_at (sqlalchemy DateTime): The datetime of ls upd.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any):it is Unused.
            **kwargs (dict): the Key/val pairs of attrs.
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, val)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """get dictionary representation 
        """
        the_dictt = self.__dict__.copy()
        the_dictt["__class__"] = str(type(self).__name__)
        the_dictt["created_at"] = self.created_at.isoformat()
        the_dictt["updated_at"] = self.updated_at.isoformat()
        the_dictt.pop("_sa_instance_state", None)
        return the_dictt

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)
