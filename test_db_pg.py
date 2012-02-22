#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, time

import psycopg2 as db
#from pyPgSQL import PgSQL as db

def insert_data(cur):
    run = True
    table = ""
    years = 0
    count_insert = 0
    cur_time = datetime.datetime(1400, 1, 1, 0, 0, 0)
    end_time = datetime.datetime(2008, 12, 31, 23, 0, 0)

    t0 = time.time()

    while run:
        if cur_time.year <= 1639:
            table = "test1"
        elif cur_time.year >= 1640 and cur_time.year <= 1679:
            table = "test2"
        elif cur_time.year >= 1680 and cur_time.year <= 1719:
            table = "test3"
        elif cur_time.year >= 1720 and cur_time.year <= 1759:
            table = "test4"
        elif cur_time.year >= 1760 and cur_time.year <= 1799:
            table = "test5"
        elif cur_time.year >= 1800 and cur_time.year <= 1839:
            table = "test6"
        elif cur_time.year >= 1840 and cur_time.year <= 1879:
            table = "test7"
        elif cur_time.year >= 1880 and cur_time.year <= 1939:
            table = "test8"
        elif cur_time.year >= 1940 and cur_time.year <= 1979:
            table = "test9"
        elif cur_time.year >= 1980:
            table = "test10"

        cur.execute("INSERT INTO " + table +
                    "(ins, date_ins, hour_ins, txt) " +
                    "VALUES(nextval('test_seq'), %s, %s, %s)",
                    ["".join([str(cur_time.year),
                            str(cur_time.month).zfill(2),
                            str(cur_time.day).zfill(2)]),
                    "".join([str(cur_time.hour).zfill(2),
                            str(cur_time.minute).zfill(2),
                            str(cur_time.second).zfill(2)]),
                    " ".join(["Testo data",
                            "/".join([str(cur_time.day).zfill(2),
                                        str(cur_time.month).zfill(2),
                                        str(cur_time.year)]),
                            "ore",
                            str(cur_time.hour)])])
        cur_time = cur_time + datetime.timedelta(hours=1)
        count_insert = count_insert + 1
        
        if count_insert == 8760:
            #print "Inserito anno " + str(cur_time.year)
            count_insert = 0
            con.commit()

        if cur_time == end_time:
            t1 = time.time()
            #print "Data corrente uguale a data di fine"
            print "Tempo di inserimento dati: %f" % (t1 - t0)
            run = False

    cur.close()

def query_data(cur):
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
    print "Inizio test"
    con = db.connect(host="localhost", database="test",
                 user="enrico", password="enrico")

    print "Inserimento dati"
    insert_data(con.cursor())

    print "Esecuzione query"
    query_data(con.cursor())

    print "Fine test"
    con.close()
