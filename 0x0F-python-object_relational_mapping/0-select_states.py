#!/usr/bin/python3
""" Listing all states from the database hbtn_0c_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)
    curr.close()
    conn.close()
