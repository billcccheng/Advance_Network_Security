#!/opt/local/bin/python

import MySQLdb
import sys

con = MySQLdb.connect(unix_socket = '/opt/local/var/run/mysql56/mysqld.sock', host = 'localhost', user = 'test_user', passwd = 'test_password', db = 'test_injection')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("CREATE TABLE Users(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
    cur.execute("INSERT INTO Users(Name) VALUES('user_1')")
    cur.execute("INSERT INTO Users(Name) VALUES('user_2')")
    cur.execute("INSERT INTO Users(Name) VALUES('user_3')")
    cur.execute("INSERT INTO Users(Name) VALUES('user_4')")
    cur.execute("INSERT INTO Users(Name) VALUES('user_5')")

    print "without proposed statement:"
    w_id = "1 OR 1=1";
    cur.execute("SELECT * FROM Users WHERE Id=%s" % (w_id))

    rows = cur.fetchall()

    for row in rows:
        print row
    print

    print "with proposed statement:"
    w_id = "1 OR 1=1";
    cur.execute("SELECT * FROM Users WHERE Id=%s", w_id)

    rows = cur.fetchall()

    for row in rows:
        print row
