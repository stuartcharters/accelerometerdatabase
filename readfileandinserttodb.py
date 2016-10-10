# script to read each csv file in directory and insert data into database table

import sqlite3 as lite
import sys
import csv
import glob
import os
import datetime

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
startdate = '' #startdate
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
                            snum = row[4:5][0]
                            print snum[5:19]
                        elif tstr[3:5] == 'St':
                            # in start time row
                            startitems = row[1:3]
                            startdate = str(startitems[0])
                            startdate = startdate.strip()
                            starttime = str(startitems[1])
                            starttime = starttime.strip()
                            h = starttime[0:2]
                            m =  starttime[3:5]
                            s =  starttime[6:]
                            basetime = datetime.time(h,m,s)
                        #    dbtime = startdate + ' ' + starttime
                        #    print dbtime
                        elif tstr[3:5] == 'Te':
                            #in temperature row]
                            temperature =  str(row[1:2][0])
                            temperature = temperature.strip()
                            print temperature
                        else:
                            pass #we don't need this header row
                    else:
                        # read accelerometer data & use info above and insert into db
                        # db table definition
                        #  TABLE movementdata(devicesn CHARACTER(15), timedate TIMESTAMP, temp REAL, x REAL, y REAL, z REAL)
                        t = row[0]
                        x = row[1]
                        y = row[2]
                        z = row[3]
                        timeincrement = datetime.timedelta(seconds=t)
                        newtime = basetime + timeincrement
                        print(basetime,t,newtime)


## db stuff - temp for reference
