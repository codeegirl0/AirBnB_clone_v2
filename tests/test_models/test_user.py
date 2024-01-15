#!/usr/bin/python3
"""Defines unnittests for models/user.py."""
import os
import pep8
import models
import MySQLdb
import unittest
from datetime import datetime
from models.base_model import Base, BaseModel
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from models.user import User


class TestUser(unittest.TestCase):
    """testing the User class"""

    @classmethod
    def setUpClass(cls):
        """User testing .
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.filestorage = FileStorage()
        cls.user = User(email="poppy@holberton.com", password="betty98")

        if type(models.storage) == DBStorage:
            cls.dbstorage = DBStorage()
            Base.metadata.create_all(cls.dbstorage._DBStorage__engine)
            Session = sessionmaker(bind=cls.dbstorage._DBStorage__engine)
            cls.dbstorage._DBStorage__session = Session()

    @classmethod
    def tearDownClass(cls):
        """User testing.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.user
        del cls.filestorage
        if type(models.storage) == DBStorage:
            cls.dbstorage._DBStorage__session.close()
            del cls.dbstorage

    def test_pep8(self):
        """Testing pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/user.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes(self):
        """Testing attrs"""
        usr = User(email="a", password="a")
        self.assertEqual(str, type(usr.id))
        self.assertEqual(datetime, type(usr.created_at))
        self.assertEqual(datetime, type(usr.updated_at))
        self.assertTrue(hasattr, (usr, "__tablename__"))
        self.assertTrue(hasattr, (usr, "email"))
        self.assertTrue(hasattr, (usr, "password"))
        self.assertTrue(hasattr, (usr, "first_name"))
        self.assertTrue(hasattr, (usr, "last_name"))
        self.assertTrue(hasattr, (usr, "places"))
        self.assertTrue(hasattr, (usr, "reviews"))

    def test_first_name(self):
        """Testing first_name"""
        User.first_name = "Arenc"
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        """Testing last_name"""

        User.last_name = "Palluqi"
        self.assertEqual(str, type(User.last_name))

    def test_docstring(self):
        """Testing docstring"""
        self.assertIsNotNone(User.__doc__)

    def test_is_subclass(self):
        """Checking amenity BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_initialize(self):
        """Testing starting"""
        self.assertIsInstance(self.user, User)

    def test_to_dict(self):
        """Testing to_dict."""
        user_dict = self.user.to_dict()
        self.assertEqual(dict, type(user_dict))
        self.assertEqual(self.user.id, user_dict["id"])
        self.assertEqual("User", user_dict["__class__"])
        self.assertEqual(self.user.created_at.isoformat(),
                         user_dict["created_at"])
        self.assertEqual(self.user.updated_at.isoformat(),
                         user_dict["updated_at"])
        self.assertEqual(self.user.email, user_dict["email"])
        self.assertEqual(self.user.password, user_dict["password"])

    @unittest.skipIf(type(models.storage) == DBStorage,
                     "Testing DBStorage")
    def test_save_filestorage(self):
        """Testing save method."""
        old = self.user.updated_at
        self.user.save()
        self.assertLess(old, self.user.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("User." + self.user.id, f.read())

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Testing FileStorage")
    def test_save_dbstorage(self):
        """Testing save method with db."""
        old = self.user.updated_at
        self.user.save()
        self.assertLess(old, self.user.updated_at)
        db = MySQLdb.connect(user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db")
        cursor = db.cursor()
        cursor.execute("SELECT * \
                          FROM `users` \
                         WHERE BINARY email = '{}'".
                       format(self.user.email))
        query = cursor.fetchall()
        self.assertEqual(1, len(query))
        self.assertEqual(self.user.id, query[0][0])
        cursor.close()

    def test_str(self):
        """Testing str rep method"""
        s = self.user.__str__()
        self.assertIn("[User] ({})".format(self.user.id), s)
        self.assertIn("'id': '{}'".format(self.user.id), s)
        self.assertIn("'created_at': {}".format(
            repr(self.user.created_at)), s)
        self.assertIn("'updated_at': {}".format(
            repr(self.user.updated_at)), s)
        self.assertIn("'email': '{}'".format(self.user.email), s)
        self.assertIn("'password': '{}'".format(self.user.password), s)


if __name__ == "__main__":
    unittest.main()
