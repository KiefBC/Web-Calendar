import pathlib

path_to_db = pathlib.Path('.', 'events.db').resolve()
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(path_to_db)
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
TESTING = True
