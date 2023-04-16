#!/usr/bin/python3

"""
A script that creates a connection to an SQL database via SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":

    args = sys.argv
    db = f"mysql+mysqldb://{args[1]}:{args[2]}@localhost/{args[3]}"

    engine = create_engine(db, pool_pre_ping=True)
    Base.metadata.create_all(engine)
