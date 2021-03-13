#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2


class JraDB:

    def __init__(self,dbname,user,pswd,host="localhost",port=5432):
        a = 1
        para = "host="+host+" port="+str(port)+" dbname="+dbname \
             + " user="+user+" password="+pswd
        self.conn = psycopg2.connect(para)
        self.cur  = self.conn.cursor()

    def search(self,sql_f):

        f = open(sql_f,"rt")

        sqls = f.read()
        sqls = sqls.replace("\n"," ")

        ret = ""
        for sql in sqls.split(";"):
            sql = sql + ";"
            if len(sql) < 5:
                continue
            self.cur.execute(sql)

            if sql[0:6] == 'select':
                ret = self.cur.fetchall()
        return ret


    def __del__(self):
        self.cur.close()
        self.conn.close()



if __name__ == '__main__':

    jraDb = JraDB("jra","postgres","root")
    a = jraDb.search("test.sql")

    print(a)

    del jraDb
