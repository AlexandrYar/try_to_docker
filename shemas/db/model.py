from sqlalchemy import MetaData, JSON, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Role(Base):
    __tablename__ = 'role'
    id = Column( Integer, primary_key=True)
    name = Column(String, nullable=False)
    premission = Column(JSON)
