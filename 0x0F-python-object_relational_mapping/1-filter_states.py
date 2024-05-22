#!/usr/bin/python3
""" script that lists all states with a name starting with N """

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    curr.execute("""SELECT * FROM states
                    WHERE name LIKE BINARY 'N%'
                    ORDER BY states.id""")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    conn.close()
