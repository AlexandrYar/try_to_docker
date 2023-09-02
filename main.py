from fastapi import FastAPI

from shemas.db.model import metadata
from service.db.db import get_all_roles, add_new_role, engine, DATABASE_URL
from shemas.db.model import Role
from service.redis.redis import set_value, get_all_value

from shemas.db.model import metadata
from service.db.db import  engine


def main():
    metadata.create_all(engine)
    print('__init__ DB is done')

app = FastAPI(title='API APP')

@app.get("/")
async def hello():
    print('__init__ DB is start, DATABASE_URL: ', DATABASE_URL)
    metadata.create_all(engine)
    print('__init__ DB is done')
    all_roles = get_all_roles()
    return all_roles


@app.post("/get_data/")
async def create_item(id, name, premission):
    role = Role()
    role.id = id
    role.name = name
    role.premission = premission

    add_new_role(role)
    return 'New role add sucsessful'
