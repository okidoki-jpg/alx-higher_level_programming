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

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")

    session.close()
