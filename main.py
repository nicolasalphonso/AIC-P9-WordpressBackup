#!/usr/bin/python

###########################################################
#
# This python script is used for wordpress backup on a ftp server
#
# Written by : Nicolas Alphonso
# Email : nicolas.alphonso@gmail.com
# Created date: Dec 05, 2021
# Tested with : Python 3.5
#
##########################################################
import os
import pipes
import time


### Variables to configure
# Mysql
DB_HOST = 'localhost'
DB_USER = 'wordpressuser'
DB_USER_PASSWORD = 'root'
DB_NAME = 'wordpressdb'
BACKUP_PATH = '/wpbackup'

# FTP

# Getting current DateTime to create the separate backup folder like "20211205-093847".
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
if not os.path.isdir(TODAYBACKUPPATH) :
    os.makedirs(TODAYBACKUPPATH)
    print("Directory `% s` created" % TODAYBACKUPPATH)

db = DB_NAME
dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
os.system(dumpcmd)
gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
os.system(gzipcmd)
