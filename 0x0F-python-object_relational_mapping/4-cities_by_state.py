#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa. """

if __name__ == '__main__':

    import MySQLdb
    import sys

    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
                 cities INNER JOIN states ON cities.state_id=states.id\
                 ORDER BY cities.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
