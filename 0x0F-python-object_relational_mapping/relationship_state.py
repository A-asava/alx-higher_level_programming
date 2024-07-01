#!/usr/bin/python3
""" python file that contains the class
    definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """State is a class representing a state in the database."""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
