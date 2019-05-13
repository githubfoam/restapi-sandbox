"""configure app to connect with database."""

from pymongo import MongoClient

DATABASE = MongoClient()['personapi'] # DB_NAME
DEBUG = True
client = MongoClient('localhost', 27017)
