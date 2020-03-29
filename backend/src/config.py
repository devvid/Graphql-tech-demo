from os.path import abspath, dirname, join
from os import environ, path

_cwd = dirname(abspath(__file__))
basedir = path.abspath(path.dirname(__file__))

class BaseConfiguration(object):
    DEBUG = True
    SECRET_KEY = 'Test'
    SQLALCHEMY_DATABASE_URI =  'sqlite:///' + path.join(basedir, 'database.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False