#!/usr/bin/python3
""" script that takes in an argument and displays
    all values in the states table of
    hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    curr.execute("""SELECT * FROM states
                    WHERE name
                    LIKE BINARY '{}'
                    ORDER BY states.id ASC""".format(sys.argv[4]))
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    conn.close()
