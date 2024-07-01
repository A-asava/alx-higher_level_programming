#!/usr/bin/python3
""" script that lists all City objects from the database
    hbtn_0e_101_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    my_cities = session.query(State).order_by(State.id)
    for instance in my_cities:
        for inst_city in instance.cities:
            print("{}: {} -> {}"
                  .format(inst_city.id, inst_city.name, instance.name))
