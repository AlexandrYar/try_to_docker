from shemas.db.model import metadata
from service.db.db import  engine


def __init__():
    metadata.create_all(engine)
    print('__init__ is done')