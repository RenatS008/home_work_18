import os


class Config(object):
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'movies.db')
