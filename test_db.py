#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, time, sys

class TestDB(object):
    _con = None
    _db = None
    _dbtype = None
    _delimiter = ""
    _user = ""
    _pwd = ""

    def __init__(self, dbtype):
        if dbtype == "mysql":
            import MySQLdb as db
            self._delimiter = "%s"
        elif dbtype == "sqlite":
            import sqlite3 as db
        else:
            raise ImportError, "database not supported"
        self._db = db
        self._dbtype = dbtype

    def set_conn_data(user=None, passwd=None):
        self._user = user
        self._pwd = passwd

    def open_connection(self, hostname=None, dbname=None):
        if not self._dbtype == "sqlite":
            self._con = self._db.connect(host=hostname, db=dbname,
                     user=self._user, passwd=self._pwd)
        else:
            self._con = self._db.connect(dbname)

    def close_connection(self):
        self._con.close()

    def create_schema(self):
        cur = self._con.cursor()
        if self._dbtype == "sqlite":
            cols = "(ins, date_ins, hour_ins, txt)"
        else:
            cols = ""

        for i in range(1, 11):
            cur.execute(" ".join(["CREATE TABLE test"+ str(i),
                                  "(ins INTEGER, date_ins INTEGER,",
                                  "hour_ins INTEGER, txt VARCHAR(30))"]))
            cur.execute("CREATE INDEX idx_test_"+ str(i) +" ON test"+ str(i) +" (date_ins)")

        cur.execute("CREATE VIEW test " + cols + " AS " +
           " UNION ".join(["SELECT ins, date_ins, hour_ins, txt FROM test1",
           "SELECT ins, date_ins, hour_ins, txt FROM test2",
           "SELECT ins, date_ins, hour_ins, txt FROM test3",
           "SELECT ins, date_ins, hour_ins, txt FROM test4",
           "SELECT ins, date_ins, hour_ins, txt FROM test5",
           "SELECT ins, date_ins, hour_ins, txt FROM test6",
           "SELECT ins, date_ins, hour_ins, txt FROM test7",
           "SELECT ins, date_ins, hour_ins, txt FROM test8",
           "SELECT ins, date_ins, hour_ins, txt FROM test9",
           "SELECT ins, date_ins, hour_ins, txt FROM test10"]))
        self._con.commit()
        cur.close()

    def insert_data(self, start, end):
        run = True
        table = ""
        years = 0
        count_insert = 0

        cur = self._con.cursor()
        t0 = time.time()

        while run:
            if start.year <= 1639:
                table = "test1"
            elif start.year >= 1640 and start.year <= 1679:
                table = "test2"
            elif start.year >= 1680 and start.year <= 1719:
                table = "test3"
            elif start.year >= 1720 and start.year <= 1759:
                table = "test4"
            elif start.year >= 1760 and start.year <= 1799:
                table = "test5"
            elif start.year >= 1800 and start.year <= 1839:
                table = "test6"
            elif start.year >= 1840 and start.year <= 1879:
                table = "test7"
            elif start.year >= 1880 and start.year <= 1939:
                table = "test8"
            elif start.year >= 1940 and start.year <= 1979:
                table = "test9"
            elif start.year >= 1980:
                table = "test10"

            cur.execute("INSERT INTO " + table +
                    "(ins, date_ins, hour_ins, txt) " +
                    "VALUES(%s, %s, %s, %s)",
                    [count_insert + 1,
                     start.strftime("%y%m%d"),
                     start.strftime("%H%M%S"),
                    " ".join(["Testo data",
                            start.strftime("%y%m%d"),
                            "ore",
                            str(start.hour)])])
            start = start + datetime.timedelta(hours=1)
            count_insert = count_insert + 1

            if count_insert == 8760:
                #print "Inserito anno " + str(start.year)
                count_insert = 0
                con.commit()

            if start == end:
                t1 = time.time()
                #print "Data corrente uguale a data di fine"
                print "Tempo di inserimento dati: %f" % (t1 - t0)
                run = False

        cur.close()

    def query_data(self):
        cur = self._con.cursor()
        t0 = time.time()
        cur.execute("select max(date_ins) from test")
        t1 = time.time()
        print "Tempo di estrazione max(date_ins): %f" % (t1 - t0)

        t2 = time.time()
        cur.execute("select * from test where date_ins between 17250101 and 17441231")
        t3 = time.time()
        print "Tempo estrazione dati dal 01/01/1725 al 31/12/1744: %f" % (t3 - t2)

        t4 = time.time()
        cur.execute("select * from test where date_ins between 17250101 and 18241231")
        t5 = time.time()
        print  "Tempo estrazione dati dal 01/01/1725 al 31/12/1824 %f" % (t5 - t4)

        t6 = time.time()
        cur.execute("select * from test where date_ins between 17250101 and 19241231")
        t7 = time.time()
        print "Tempo estrazione dati dal 01/01/1725 al 31/12/1924 %f" % (t7 - t6)

        cur.close()

if __name__ == "__main__":
    t = TestDB(sys.argv[1])

    print "Inizio test database " + sys.argv[1]
    if not sys.argv[1] == "sqlite":
        t.set_conn_data(user=sys.argv[4], passwd=sys.argv[5])
        t.open_connection(hostname=sys.argv[2], dbname=sys.argv[3])
    else:
        t.open_connection(dbname=sys.argv[2])

    print "Creazione schema"
    t.create_schema()

    print "Inserimento dati"
    t.insert_data(start=datetime.datetime(1400, 1, 1, 0, 0, 0),
                  end=datetime.datetime(2008, 12, 31, 23, 0, 0))

    print "Esecuzione query"
    t.query_data()

    print "Fine test"
    t.close_connection()
