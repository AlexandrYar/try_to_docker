from shemas.db.model import metadata, Role
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os, json
import logging


DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)
session = Session()



def add_new_role(new_role: Role):
    session.add(new_role)
    logging.info('ADD NEW ROLE')
    session.commit()

def get_all_roles():
    all_roles_query = session.query(Role).all()
    all_roles = {}
    for i in all_roles_query:
        all_roles[i.id]={
            'name': i.name,
            'premission': i.premission
        }
    return all_roles

    