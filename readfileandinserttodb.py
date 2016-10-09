# script to read each csv file in directory and insert data into database table

import sqlite3 as lite
import sys
import csv
import glob
import os

# database connection variable
con = None
# path to sqlite3 db
db = '/home/stuart/cqu/cquaccdata.db'
# directory of the datafiles
directry = '/home/stuart/cqu/'
#connect to database
con = lite.connect(db)

# holding variable for header info
snum = '' # serial number
starttime = '' # starttime
temperature = '' # temperature read by device at data capture start


# foreach csv in directory
# open and read header lines
# save to variables
# the read each data variable line
# insert into db.
with con:
    cur = con.cursor()
    os.chdir(directry)
    for file in glob.glob("*.CSV"):
        with open(file,'rb') as csvfile:
            for row in csv.reader(csvfile):
                    tstr = str(row[:1])
                    if tstr[2:3]==';':
                        if tstr[3:4] == 'V':
                            # in version number header row
                            print row
                        elif tstr[3:5] == 'St':
                            # in start time row
                            print row
                        elif tstr[3:5] == 'Te':
                            #in temperature row]
                            print row
                        else:
                            pass #we don't need this header row        
                    else:
                        # read accelerometer data & use info above and insert into db
                        # db table definition
                        #  TABLE movementdata(devicesn CHARACTER(15), timedate TIMESTAMP, temp REAL, x REAL, y REAL, z REAL)


## db stuff - temp for reference
