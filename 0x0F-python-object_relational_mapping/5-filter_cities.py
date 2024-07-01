#!/usr/bin/python3
"""
    script that takes in the name of a state as
    an argument and lists all cities of that state, using the
    database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    search = sys.argv[4]
    curr.execute("""SELECT cities.name FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    WHERE states.name LIKE %s
                    ORDER BY cities.id ASC""", (search, ))
    query_rows = curr.fetchall()
    list_row = []
    for row in query_rows:
        list_row.append(row[0])
    print(*list_row, sep=", ")
    curr.close()
    conn.close()
