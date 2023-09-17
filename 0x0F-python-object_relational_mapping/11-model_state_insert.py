#!/usr/bin/python3
"""
script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
i"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access the database
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
