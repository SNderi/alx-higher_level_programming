#!/usr/bin/python3
""" A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa that is safe from MySQL injections. """

if __name__ == '__main__':

    import MySQLdb
    import sys

    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name=%s\
                ORDER BY id", (args[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
