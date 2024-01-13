#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py (mysql username, mysql password, database name)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM `states`"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
