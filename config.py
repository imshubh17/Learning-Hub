import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'6\xe9\xda\xead\x81\xf7\x8d\xbbH\x87\xe8m\xdd3%'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/learninghub'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    