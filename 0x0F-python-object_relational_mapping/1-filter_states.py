#!/usr/bin/python3
"""
A script that lists all states with a name starting with N(Upper N)
from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py user passwd hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM `states` ORDER BY `id`"
    cur.execute(query)
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
