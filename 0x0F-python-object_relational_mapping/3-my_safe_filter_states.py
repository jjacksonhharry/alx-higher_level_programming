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
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s "
                      "ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
