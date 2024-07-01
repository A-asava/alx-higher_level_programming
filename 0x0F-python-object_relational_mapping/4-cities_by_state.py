#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    curr.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states
                    ON cities.state_id = states.id
                    ORDER BY cities.id""")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    conn.close()
