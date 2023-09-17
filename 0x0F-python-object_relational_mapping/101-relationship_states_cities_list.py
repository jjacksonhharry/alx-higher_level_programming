#!/usr/bin/python3
"""
script that deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """
    Access the database
    """
    if len(sys.argv) != 4:
        print("Usage: {} <DB_USER> <DB_PASSWORD> <DB_NAME>".format(sys.argv[0]))
        sys.exit(1)

    db_user, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(db_user, db_password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
