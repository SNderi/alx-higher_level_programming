#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa. """

if __name__ == '__main__':

    import MySQLdb
    import sys

    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
                 cities.state_id=states.id WHERE states.name=%s\
                 ORDER BY cities.id;", (args[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
