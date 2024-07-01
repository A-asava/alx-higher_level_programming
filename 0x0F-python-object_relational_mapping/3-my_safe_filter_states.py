#!/usr/bin/python3
"""
    script that takes in arguments and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    search = sys.argv[4]
    curr.execute("""SELECT * FROM states
                    WHERE name
                    LIKE %s
                    ORDER BY states.id ASC""", (search, ))
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    conn.close()
