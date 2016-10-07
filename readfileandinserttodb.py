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
                    str = row[:1]
                    print str[:1]
                    sys.exit(0)
#                    if row[:1]==';':
#                        print row


## db stuff - temp for reference
