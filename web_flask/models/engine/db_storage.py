#!/usr/bin/python3
"""DB Storage Engine"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """create tables in env"""

    __engine = None
    __session = None
    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+msqldb://{}:{}@{}/{}'.format(user, passwd, host, db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dic
        return : return a dic of __obj
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            qu = self.__session.query(cls)
            for el in qu:
                key = "{}.{}".format(type(el).__name__, el.id)
                dic[key] = el
        else:
            li = [State, City, User, Place, Review, Amenity]
            for c in li:
                q = self.__session.query(c)
                for e in q:
                    k = "{}.{}".format(type(e).__name__, e.id)
                    dic[k] = e

        return (dic)
    
    def new(self, obj):
         """add a new element in the table
        """
         self.__session.add(obj)

    def save(self):
        """save chnage
        """
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete the ele
        """
        if obj:
            self.__session.__delete(obj)
    def reload(self):
        """config
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()
    
    def close(self):
        """closeremove()
        """
        self.__session.close()
        