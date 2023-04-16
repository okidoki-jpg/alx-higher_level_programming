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

    """ execute, read and display query: names matching search arg"""
    c.execute("SELECT * FROM states WHERE name = {}".format(search))
    [print(i) for i in c.fetchall()]
    c.close()
    conn.close()
