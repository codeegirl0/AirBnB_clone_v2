#!/usr/bin/python3
"""db storage file"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from os import getenv


class DBStorage:
    """class of db storage 
    Attr: __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """creating engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """get on the currect db session"""
        objects_dictionary = {}

        if cls is None:
            objects_list = self.__session.query(State).all()
            objects_list.extend(self.__session.query(City).all())
            objects_list.extend(self.__session.query(User).all())
            objects_list.extend(self.__session.query(Place).all())
            objects_list.extend(self.__session.query(Amenity).all())
            objects_list.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects_list = self.__session.query(cls).all()

        for obj in objects_list:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dictionary[key] = obj

        return objects_dictionary

    def new(self, obj):
        """adding object to db session"""
        self.__session.add(obj)

    def save(self):
        """linking  current db session"""

        self.__session.commit()

    def delete(self, obj=None):
        """remove in  database
        session obj if it is not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creating tables in the database"""

        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()

    def close(self):
        """closing session"""
        self.__session.close()
