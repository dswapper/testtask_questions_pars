import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_JSERVICE_REQUESTS = 100 # due to https://jservice.io/ max questions is 100
    MAX_WHILE_REQUESTS_DEPTH = 5