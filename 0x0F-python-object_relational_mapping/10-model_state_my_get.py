#!/usr/bin/python3
""" script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    search = sys.argv[4]
    states = session.query(State).filter(State.name == search).first()

    try:
        print(states.id)
    except AttributeError:
        print("Not found")
