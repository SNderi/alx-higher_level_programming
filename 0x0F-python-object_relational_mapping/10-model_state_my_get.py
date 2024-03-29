#!/usr/bin/python3
""" A script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa. """

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    request = session.query(State).filter(State.name == sys.argv[4]).scalar()
    if request:
        print("{}".format(request.id))
    else:
        print("Not found")
    session.close()
