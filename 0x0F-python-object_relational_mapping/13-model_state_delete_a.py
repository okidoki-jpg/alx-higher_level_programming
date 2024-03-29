#!/usr/bin/python3

"""
A script that connects to an SQL database via SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    args = sys.argv
    db = f"mysql+mysqldb://{args[1]}:{args[2]}@localhost:3306/{args[3]}"

    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
