#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database
    """
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                            FROM cities JOIN states ON cities.state_id \
                            = states.id ORDER BY cities.id ASC")

        rows_selected = db_cursor.fetchall()

        for row in rows_selected:
            print(row)
