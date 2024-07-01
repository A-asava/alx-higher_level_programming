#!/usr/bin/python3
""" Script that prints all City objects from the
    database hbtn_0e_14_usa:"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = (session.query(State.name, City.id, City.name)
              .join(City, City.state_id == State.id).all())
    for instance in cities:
        print("{}: ({}) {}".format(*instance))
