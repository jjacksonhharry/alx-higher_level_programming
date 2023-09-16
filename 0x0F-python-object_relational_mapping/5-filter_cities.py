#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name FROM cities"
                          "JOIN states ON cities.state_id = states.id"
                          "WHERE states.name LIKE BINARY %(state_name)s"
                          "ORDER BY cities.id ASC", {'STATE_NAME': ARGV[4]})

        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
