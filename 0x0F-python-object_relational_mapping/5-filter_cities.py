#!/usr/bin/python3

"""
A script connecting to an SQL database
"""

import sys
from MySQLdb import connect

if __name__ == "__main__":

    args = sys.argv
    search = args[4]

    """ connect to database """
    conn = connect(host="localhost",
                   user=args[1],
                   password=args[2],
                   database=args[3],
                   port=3306)

    """ create cursor """
    c = conn.cursor()

    """ execute, read and display query: cities in a given state """
    c.execute("SELECT cities.name FROM cities\
             JOIN states ON cities.state_id = states.id\
              WHERE states.name LIKE %s", (search,))
    print(*[i[0] for i in c.fetchall()], sep=", ")
    c.close()
    conn.close()
