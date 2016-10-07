# Stuart Charters October 2016
# code to create sqlite3 database tables for accelerometer data
# to take data for the http://www.gcdataconcepts.com/x16-4.html

import sqlite3 as lite
import sys

con = None
db = '/home/stuart/cqu/cquaccdata.db'

try:
    con = lite.connect(db)

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLite version: %s" % data

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    
    if con:
        con.close()
