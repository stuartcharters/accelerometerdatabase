# Stuart Charters October 2016
# code to create sqlite3 database tables for accelerometer data
# to take data for the http://www.gcdataconcepts.com/x16-4.html

import sqlite3 as lite
import sys

con = None
db = '/home/stuart/cqu/cquaccdata.db'


con = lite.connect(db)
with con:
    cur = con.cursor()
    # get the sqlite3 version number to check db connection is working correctly
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()
    #print out the version
    print "SQLite version: %s" % data
    #create the datatable
    # table name is movementdata
    # col names
    # devicesn = device serial number - so you know which device it was from - and can link back to a cow
    # timedate = time of the data recording - integer in seconds from 1/1/1970 00:00:00 UTC
    # temp = temperature as recorded by device in oC to two decimal places
    # x = x-axis accelerometer reading
    # y = y-axis accelerometer reading
    # z = z-axis accelerometer reading
    cur.execute("CREATE TABLE movementdata(devicesn CHARACTER(15), timedate TIMESTAMP, temp REAL, x REAL, y REAL, z REAL)")
