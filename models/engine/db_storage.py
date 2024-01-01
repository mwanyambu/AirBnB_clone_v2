#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ as env


"""classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }"""


class DBStorage:
    """This class serializes instances for database storage
    Attributes:
        __engine: engin to connect db
        __session: session to interact with db
        __clsdict: dictionary of all classes
    """
    __engine = None
    __session = None
    __clsdict = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """setup __engine
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                env['HBNB_MYSQL_USER'],
                env['HBNB_MYSQL_PWD'],
                env['HBNB_MYSQL_HOST'],
                env['HBNB_MYSQL_DB']
            ), pool_pre_ping=True
        )
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        if env.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query for objects depend on the class
        Arguments:
            cls: class to query
        """
        d = {}
        cls = cls if not isinstance(cls, str) else self.__clsdict.get(cls)
        if cls:
            for obj in self.__session.query(cls):
                d["{}.{}".format(cls.__name__, obj.id)] = obj
            return (d)
        for key, cls in self.__clsdict.items():
            for obj in self.__session.query(cls):
                d["{}.{}".format(cls.__name__, obj.id)] = obj
        return (d)
        """for classs in classes:
            if classs is None or cls is classes[classs] or cls is classs:
                keyvals = self.__session.query(classes[classs]).all()
                for keyval in keyvals:
                    key = keyval.__class__.__name__ + '.' + keyval.id
                    d[key] = keyval
        return (d)"""

    def new(self, obj):
        """add an object to current db session
        Arguments:
            obj: object to add
        """
        if obj and self.__session:
            self.__session.add(obj)

    def save(self):
        """commit all changes of current db session
        """
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current db session
        Arguments:
            obj: object to delete
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        try:
            Base.metadata.create_all(self.__engine)
            factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(factory)()
        except Exception as e:
            print(e)

    def close(self):
        """remove current session and roll back all unsaved transactions
        """
        if self.__session:
            self.__session.close()
